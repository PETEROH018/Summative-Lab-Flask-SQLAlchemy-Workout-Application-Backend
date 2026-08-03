from marshmallow import fields,validate,ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import *

class Exercise_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        sqla_session = db.session

    category = fields.Str(validate=validate.Length(min=4,max=30,error="The category should be 4 to 30 characters long"))
    equipment_needed = fields.Boolean(truthy={'True','true','Yes','yes','Y','y'}, falsy={'False','false','No','no','N','n'}, error_messages={"invalid":"equipment needed should be a boolean answer like True,False or Yes,No or Y,N or y,n or yes,no"})
    workoutexercises = fields.Nested("WorkoutExercise_Schema", many=True, exclude=('exercise','workout_id','exercise_id','id'))

class WorkoutExercise_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True
    
    exercise = fields.Nested("Exercise_Schema", exclude=('workoutexercises',))
    workout = fields.Nested("Workout_Schema", exclude=('workoutexercises',))

class Workout_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    notes = fields.Str(validate=validate.Length(min=5,max=50,error="The notes should be 5 to 50 characters long"))
    workoutexercises = fields.Nested("WorkoutExercise_Schema", many=True , exclude=('id','exercise_id','workout_id','workout'))