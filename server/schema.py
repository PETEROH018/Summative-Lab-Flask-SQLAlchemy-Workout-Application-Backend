from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import *

class Exercise_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        sqla_session = db.session

class WorkoutExercise_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

    exercise = fields.Nested("Exercise_Schema")

class Workout_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    workoutexercises = fields.Nested("WorkoutExercise_Schema", many=True , exclude=('id','exercise_id','workout_id','workout'))