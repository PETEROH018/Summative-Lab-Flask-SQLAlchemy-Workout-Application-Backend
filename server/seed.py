#!/usr/bin/env python3

from app import app
from models import *

with app.app_context():
    Exercise.query.delete()
    Workout.query.delete()

    exercises = []
    workouts = []

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

    db.session.add_all(exercises)
    db.session.add_all(workouts)
    db.session.commit()


