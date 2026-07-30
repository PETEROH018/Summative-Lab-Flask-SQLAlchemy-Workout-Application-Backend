from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import *

class Workout_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True


