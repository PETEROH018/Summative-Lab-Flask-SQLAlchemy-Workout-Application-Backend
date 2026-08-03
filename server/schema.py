from marshmallow import fields,validate,ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import *

# This schema is used to serialize and deserialize exercise data
class Exercise_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        sqla_session = db.session

    # This is schema level validation of the category field
    category = fields.Str(validate=validate.Length(min=4,max=30,error="The category should be 4 to 30 characters long"))
    # This is schema level validation of the equipment_needed field
    equipment_needed = fields.Boolean(truthy={'True','true','Yes','yes','Y','y'}, falsy={'False','false','No','no','N','n'}, error_messages={"invalid":"equipment needed should be a boolean answer like True,False or Yes,No or Y,N or y,n or yes,no"})
    # This class attribute is used for nesting multiple workoutexercises inside a single exercise
    workoutexercises = fields.Nested("WorkoutExercise_Schema", many=True, exclude=('exercise','workout_id','exercise_id','id'))

class WorkoutExercise_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

    # This class attribute is used for nesting a single exercise inside a workoutexercise when getting the exercises assigned to a given workout
    # exclude workoutexercises is used to prevent an infinite recursion which might cause the application to crash
    exercise = fields.Nested("Exercise_Schema", exclude=('workoutexercises',))
    # This class attribute is used for nesting a single workout inside a workoutexercise when getting the workouts that a given exercise is has been assigned to
    # exclude workoutexercises is used to prevent an infinite recursion which might cause the application to crash
    workout = fields.Nested("Workout_Schema", exclude=('workoutexercises',))

class Workout_Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    # This is schema level validation of the notes field
    notes = fields.Str(validate=validate.Length(min=5,max=50,error="The notes should be 5 to 50 characters long"))
    # This class attribute is used for nesting multiple workoutexercises inside a single workout
    workoutexercises = fields.Nested("WorkoutExercise_Schema", many=True , exclude=('id','exercise_id','workout_id','workout'))