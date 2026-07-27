from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Exercise(db.Model):
    __table__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    category = db.Column(db.String(20), nullable = False)
    equipment_needed = db.Column(db.Boolean, nullable = False)

    workoutexercise = db.relationship('WorkoutExercise',backpopulates='exercise', cascade= 'all delete-orphan')

    

class Workout(db.Model):
    __table__ = 'workouts'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    duration_minutes = db.Column(db.Integer, nullable =False)
    notes = db.Column(db.String(50))

    workoutexercise = db.relationship('WorkoutExercise',backpopulates='workout', cascade= 'all delete-orphan')


'''This is a joining table that joins the workouts table and the exercises table because they have a many-to-many relationship'''
class WorkoutExercise(db.Model):
    __table__ = 'workoutexercises'

    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Integer,db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer,db.ForeignKey('exercises.id'))
    reps = db.Column(db.Integer, nullable = False)
    sets = db.Column(db.Integer, nullable = False)
    duration_seconds = db.Column(db.Integer, nullable = False)

    exercise = db.relationship('Exercise',backpopulates = 'workoutexercise')
    workout = db.relationship('Workout',backpopulates = 'workoutexercise')