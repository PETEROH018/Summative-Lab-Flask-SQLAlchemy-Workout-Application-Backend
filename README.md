# Flask SQLAlchemy Workout Application Backend

## Description
- This is a workout application that is used to assign exercises to workouts
- A single workout can have multiple exercises plus details about the workout date, workout duration in minutes and some notes about the workout
- A single exercise can be in multiple workouts and includes details about the exercise name, exercise category and a boolean value of whether exercise equipment is needed
- Since the workouts and exercises have a many to many relationship, a workoutexercise table is used as the joining table and also includes details about repetitions(reps),sets and the duration in seconds of each workoutexercise

## Installation Instructions
- The dependecies needed for this project are listed in the requirements.txt file
- To install these dependencies:
    1. Navigate to this application's root directory
    2. Create a python virtual environment by running pipenv shell on the terminal
    3. Install the dependecies listed in the requirements.txt file by running pipenv install -r requirements.txt on the virtual environment terminal
    4. A pipfile text file will be created listing all the packages that have been installed and an accompanying pipfile.lock JSON file which locks down all the exact versions of packages that have been installed and cryptographically hashes them to prevent unathorized modification of the package versions

## Database Migration Instructions
- This project uses Alembic that is wrapped in Flask-Migrate for tracking the database versions allowing upgrading and rolling back of any changes to the database schema
- The database schema is the blueprint that indicates the tables, columns and the relationships between tables in the database
- To set up the migration environment, follow these steps:
    1. Inside the virtual environment created earlier, run flask db init on the terminal
    2. Run flask db migrate -m "Initial migration" on the terminal to create migration scripts
    3. Run flask db upgrade head on the terminal to run the migration scripts and update the database schema

## Database Seeding Instructions
- Seeding the database is generating sample data in the database during developments and testing
- A seed file exists in the server folder and to run the seeding script:
    1. Inside the virtual environment, navigate to the server folder
    2. Run 'python3 seed.py' in the terminal
    3. Inside the server folder, open the instance folder to see the database file, app.db
    4. Open the database file with an SQLite database viewer VS Code extension to see the generated sample data

## Flask Application Running and Operation Instructions
### Running
- To run the flask app, ensure you are in the server folder while inside the virtual environments then run 'flask run' on the terminal
- This starts a flask development server and generates a URL that you can copy and paste on a browser or an API testing platform like POSTMAN. The URL may differ based on the port that the flask app is running on. It might be 'http://127.0.0.1:5000' or 'http://127.0.0.1:5555'

### Operation
- There are 9 endpoints used for CRD operations on the database created and seeded earlier
- They include:
    1. GET /workouts for listing all workouts
    2. GET /workouts/<id> for showing a single workout with its associated exercises including reps/sets/duration data from WorkoutExercises
    3. POST /workouts for creating a workout
    4. DELETE /workouts/<id> for deleting a workout and associated WorkoutExercises
    5. GET /exercises for listing all exercises
    6. GET /exercises/<id> for showing an exercise with its associated workouts including reps/sets/duration data from WorkoutExercises
    7. POST /exercises for creating an exercise
    8. DELETE /exercises/<id> for deleting an exercise and associated WorkoutExercises
    9. POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises for adding an exercise to a workout, including reps/sets/duration

- To do a GET request for all workouts, select GET method on POSTMAN and use the URL 'http://127.0.0.1:5000/workouts'
- To do a GET request for all exercises, select GET method on POSTMAN and use the URL 'http://127.0.0.1:5000/exercises'
- To do a GET request for a workout with id 1, select GET method on POSTMAN and use the URL 'http://127.0.0.1:5000/workouts/1'
- To do a GET request for an exercise with id 1, select GET method on POSTMAN and use the URL 'http://127.0.0.1:5000/exercises/1'
- To do a POST request for a new workout, select POST method on POSTMAN and use the URL 'http://127.0.0.1:5000/workouts'. Then add a JSON payload specifying the date in 'YYYY-MM-DD' format, the workout duration in minutes and a brief note about the workout
- To do a POST request for a new exercise, select POST method on POSTMAN and use the URL 'http://127.0.0.1:5000/exercises'. Then add a JSON payload specifying the exercise name, exercise category and a boolean that indicates whether the exercise requires equipment (equipment_needed)
- To do a POST request for a workout exercise for workout with id 1 and exercise with id 1, select POST method on POSTMAN and use the URL 'http://127.0.0.1:5000/workouts/1/exercises/1/workout_exercises'. Then specify the number of repetitions(reps),sets and the duration in seconds of the workout exercise
- To do a DELETE request for a workout with id 1, select DELETE method on POSTMAN and use the URL 'http://127.0.0.1:5000/workouts/1'
- To do a DELETE request for an exercise with id 1, select DELETE method on POSTMAN and use the URL 'http://127.0.0.1:5000/exercises/1'