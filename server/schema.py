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
