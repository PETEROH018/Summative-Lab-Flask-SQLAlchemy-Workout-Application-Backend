from flask import Flask, make_response,request
from flask_migrate import Migrate

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
    workout = db.session.get(Workout,id)
    if workout:
        workout_schema = Workout_Schema()
        return make_response(workout_schema.dump(workout),200)
    else:
        return make_response({"error":f"No workout with id: {id}"},404)

@app.route('/workouts',methods=['POST'])
def add_workout():
    data = request.get_json()
    new_workout = Workout(date=data["date"],duration_minutes=data["duration_minutes"],notes=data["notes"])
    db.session.add(new_workout)
    db.session.commit()
    return make_response({"message":"Added new workout"})

@app.route('/workouts/<id>',methods=['DELETE'])
def remove_workout(id):
    workout = db.session.get(Workout,id)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return make_response({"message":"Workout deleted successfully"},200)
    else:
        return make_response({"error":f"No workout with id: {id}"},404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)