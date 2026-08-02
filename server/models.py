from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import re
from datetime import datetime
db = SQLAlchemy()
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    category = db.Column(db.String(20), nullable = False)
    equipment_needed = db.Column(db.Boolean, nullable = False)

    workoutexercises = db.relationship('WorkoutExercise',back_populates='exercise', cascade= 'all, delete-orphan')

    @validates('name')
    def validate_name(self,key,value):
    
        if not re.match(r'^[a-zA-Z ]+$',value):
            raise ValueError("The name of the exercise should only contain letters and spaces!")
        return value
    
class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Text, nullable = False)
    duration_minutes = db.Column(db.Integer, nullable =False)
    notes = db.Column(db.String(50))

    workoutexercises = db.relationship('WorkoutExercise',back_populates='workout', cascade= 'all, delete-orphan')

    @validates('date')
    def validate_date(self,key,value):
        try:
            datetime.strptime(value,"%Y-%m-%d")
        except ValueError:
            raise ValueError("The date should be in the format YYYY-MM-DD")
        return value

'''This is a joining table that joins the workouts table and the exercises table because they have a many-to-many relationship'''
class WorkoutExercise(db.Model):
    __tablename__ = 'workoutexercises'

    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Integer,db.ForeignKey('workouts.id'),nullable=False)
    exercise_id = db.Column(db.Integer,db.ForeignKey('exercises.id'),nullable=False)
    reps = db.Column(db.Integer, nullable = False)
    sets = db.Column(db.Integer, nullable = False)
    duration_seconds = db.Column(db.Integer, nullable = False)

    exercise = db.relationship('Exercise',back_populates = 'workoutexercises')
    workout = db.relationship('Workout',back_populates = 'workoutexercises')