from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import *

class Workout_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        sqla_session = db.session

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
