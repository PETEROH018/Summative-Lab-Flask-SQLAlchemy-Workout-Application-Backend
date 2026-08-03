#!/usr/bin/env python3

from app import app
from models import *

with app.app_context():
    '''This section handles clearing the database tables to prevent duplicating data each time the database is seeded'''
    Exercise.query.delete()
    Workout.query.delete()
    WorkoutExercise.query.delete()

    '''This section handles declaring new lists that will hold the database table records inform of model objects'''
    exercises = []
    workouts = []
    workoutexercises = []

    '''This section handles creating the model objects and appending them to their respective list'''
    exercises.append(Exercise(name="Push ups",category="Upper Body / Strength",equipment_needed=False))
    exercises.append(Exercise(name="Squats",category="Lower Body / Strength",equipment_needed=False))
    exercises.append(Exercise(name="Plank",category="Core / Stability",equipment_needed=False))
    exercises.append(Exercise(name="Dumbbell Bicep Curl",category="Upper Body / Strength",equipment_needed=True))
    exercises.append(Exercise(name="Jump Rope",category="Cardio / Endurance",equipment_needed=True))

    workouts.append(Workout(date="2026-07-30", duration_minutes=45, notes="Focused on upper body strength, completed all sets."))
    workouts.append(Workout(date="2026-07-31", duration_minutes=30, notes="High-intensity cardio session, felt energized."))
    workouts.append(Workout(date="2026-08-01", duration_minutes=60, notes="Leg day, increased weight on squats."))
    workouts.append(Workout(date="2026-08-02", duration_minutes=20, notes="Quick core and stability routine before work."))
    workouts.append(Workout(date="2026-08-03", duration_minutes=50, notes="Full body conditioning, good recovery pace."))

    workoutexercises.append(WorkoutExercise(workout_id=1, exercise_id=1, reps=15, sets=3, duration_seconds=0))   # Push-ups in Workout 1
    workoutexercises.append(WorkoutExercise(workout_id=2, exercise_id=5, reps=0, sets=3, duration_seconds=180))  # Jump Rope in Workout 2
    workoutexercises.append(WorkoutExercise(workout_id=3, exercise_id=2, reps=12, sets=4, duration_seconds=0))   # Squats in Workout 3
    workoutexercises.append(WorkoutExercise(workout_id=4, exercise_id=3, reps=1, sets=3, duration_seconds=60))   # Plank in Workout 4
    workoutexercises.append(WorkoutExercise(workout_id=5, exercise_id=4, reps=10, sets=4, duration_seconds=0))   # Bicep Curls in Workout 5

    '''This section handles populating the database with the sample data'''
    db.session.add_all(exercises)
    db.session.add_all(workouts)
    db.session.add_all(workoutexercises)
    db.session.commit()
    


