from flask import Flask, make_response,request
from flask_migrate import Migrate
from sqlalchemy.orm import selectinload


from models import *
from schema import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/workouts',methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    if workouts:
        # When many is set to True, Workout_Schema handles serializing all workout python objects without having to manually loop through them
        # Excluding workoutexercises ensures that only details about the workout are displayed without including details about the associated workoutexercises
        workouts_schema = Workout_Schema(many=True,exclude=('workoutexercises',))
        return make_response(workouts_schema.dump(workouts))
    else:
        return make_response({"error":"No workouts to show"})

@app.route('/workouts/<id>',methods=['GET'])
def get_workout(id):
    # selectinload method is used to nest multiple workoutexercises inside a single workout in the first argument
    # selectinload is also used to nest a single exercise into each workoutexercise in the second argument
    # This creates a nested python object
    workout = db.session.get(Workout,id,options=[selectinload(Workout.workoutexercises,WorkoutExercise.exercise)])
    if workout:
        # Workout_Schema is used to serialize the nested pyton object (workout)
        workout_schema = Workout_Schema()
        return make_response(workout_schema.dump(workout),200)
    else:
        return make_response({"error":f"No workout with id: {id}"},404)

@app.route('/workouts',methods=['POST'])
def add_workout():
    data = request.get_json()
    workout_schema = Workout_Schema()
    # The .load schema method handles the deserialization from a python dictionary(data) to a python object of the Workout model
    new_workout = workout_schema.load(data)
    db.session.add(new_workout)
    db.session.commit()
    return make_response({"message":"Added a new workout"},201)

@app.route('/workouts/<id>',methods=['DELETE'])
def remove_workout(id):
    workout = db.session.get(Workout,id)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return make_response({"message":"Workout deleted successfully"},200)
    else:
        return make_response({"error":f"No workout with id: {id}"},404)

@app.route('/exercises',methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    if exercises:
        # When many is set to True, Exercise_Schema handles serializing all exercise python objects without having to manually loop through them
        # Excluding workoutexercises ensures that only details about the exercise are displayed without including details about the associated workoutexercises
        exercises_schema = Exercise_Schema(many=True,exclude=('workoutexercises',))
        return make_response(exercises_schema.dump(exercises))
    else:
        return make_response({"error":"No exercises to show"})

@app.route('/exercises/<id>',methods=['GET'])
def get_exercise(id):
    # selectinload method is used to nest multiple workoutexercises inside a single exercise in the first argument
    # selectinload is also used to nest a single workout into each workoutexercise in the second argument
    # This creates a nested python object
    exercise = db.session.get(Exercise,id,options=[selectinload(Exercise.workoutexercises,WorkoutExercise.workout)])
    if exercise:
        #Exercise_Schema is used to serialize the nested pyton object (exercise)
        exercise_schema = Exercise_Schema()
        return make_response(exercise_schema.dump(exercise),200)
    else:
        return make_response({"error":f"No exercise with id: {id}"},404)

@app.route('/exercises',methods=['POST'])
def add_exercise():
    data = request.get_json()
    exercise_schema = Exercise_Schema()
    # The .load schema method handles the deserialization from a python dictionary(data) to a python object of the Exercise model
    new_exercise=exercise_schema.load(data)
    db.session.add(new_exercise)
    db.session.commit()
    return make_response({"message":"Added a new exercise"})

@app.route('/exercises/<id>',methods=['DELETE'])
def remove_exercise(id):
    exercise = db.session.get(Exercise,id)
    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        return make_response({"message":"Exercise deleted successfully"},200)
    else:
        return make_response({"error":f"No exercise with id: {id}"},404)

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises',methods=['POST'])
def add_workoutexercise(workout_id,exercise_id):
    data={"workout_id":int(workout_id),"exercise_id":int(exercise_id),**request.get_json()}
    print(data)
    workoutexercise_schema = WorkoutExercise_Schema()
    # The .load schema method handles the deserialization from a python dictionary(data) to a python object of the WorkoutExercise model
    new_workoutexercise=workoutexercise_schema.load(data)
    db.session.add(new_workoutexercise)
    db.session.commit()
    return make_response({"message":"Added a new workout exercise"})

# The @app.errorhandler decorator is used here to catch ValueError exceptions that happen on the model level and parse them into JSON format that can be cleanly sent to a client
@app.errorhandler(ValueError)
def handle_validation_error(error):
    response_body = {
        "error": "Input Validation Failed",
        "message": error.args[0] if error.args else "Invalid data provided."
    }
    return make_response(response_body, 400)

# The @app.errorhandler decorator is used here to catch ValidationError exceptions that happen on the schema level and parse them into JSON format that can be cleanly sent to a client
@app.errorhandler(ValidationError)
def handle_marshmallow_validation_error(error):
    return make_response({"error": "Input Validation Failed", "message": error.messages}, 400)



if __name__ == '__main__':
    app.run(port=5555, debug=True)