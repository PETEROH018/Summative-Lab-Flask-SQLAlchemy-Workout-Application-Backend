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
        workouts_schema = Workout_Schema(many=True)
        return make_response(workouts_schema.dump(workouts))
    else:
        return make_response({"error":"No workouts to show"})

@app.route('/workouts/<id>',methods=['GET'])
def get_workout(id):
    workout = db.session.get(Workout,id,options=[selectinload(Workout.workoutexercises,WorkoutExercise.exercise)])
    if workout:
        workout_schema = Workout_Schema()
        return make_response(workout_schema.dump(workout),200)
    else:
        return make_response({"error":f"No workout with id: {id}"},404)

@app.route('/workouts',methods=['POST'])
def add_workout():
    data = request.get_json()
    workout_schema = Workout_Schema()
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
        exercises_schema = Exercise_Schema(many=True)
        return make_response(exercises_schema.dump(exercises))
    else:
        return make_response({"error":"No exercises to show"})

@app.route('/exercises/<id>',methods=['GET'])
def get_exercise(id):
    exercise = db.session.get(Exercise,id)
    if exercise:
        exercise_schema = Exercise_Schema()
        {"id":exercise.id,"name":exercise.name,"category":exercise.category}
        return make_response(exercise_schema.dump(exercise),200)
    else:
        return make_response({"error":f"No exercise with id: {id}"},404)

@app.route('/exercises',methods=['POST'])
def add_exercise():
    data = request.get_json()
    exercise_schema = Exercise_Schema()
    # new_exercise = Exercise(name=data["name"],category=data["category"],duration_seconds=data["duration"])
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
    new_workoutexercise=workoutexercise_schema.load(data)
    db.session.add(new_workoutexercise)
    db.session.commit()
    return make_response({"message":"Added a new workout exercise"})


if __name__ == '__main__':
    app.run(port=5555, debug=True)