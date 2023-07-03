# Setting up imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db,Student

# Setting up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
db.init_app(app)

# Now lets run int the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5555
    # flask db init
    # flask db revision --autogenerate -m 'Create tables productions'
    # flask db upgrade

# Lets create some Seed data!

# We can run the server with flask run and navigate to http://localhost:5555/`

# Routes
    # We can set up routes with @app.route('/')
    # Now lets set up a route that goes to the following image
    # If we have a dynamic route we can use 
        # @app.route('/<title>')
        #  def display(title):
        #     return f'<h1>{title}</h1>'
    # Lets use the class.query.filter() in order to filter like we were using
    # sqlAlchemy
#Hi
@app.route('/')
def diplayRoute():
    return f'<div>Hello World<div>'

@app.route('/students')
def displayStudents():
    students = Student.query.all()
    print("All students: ", students)
    all_students_dict = []
    for student in students:
        student_dict = {
        "name": student.name,
        "code": student.student_code
        }
        all_students_dict.append(student_dict)
    return all_students_dict

@app.route('/students/<id>')
def displaySingleStudents(id):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        return make_response({"Error": "Learn to type nerd"},400)
    print("Student: ", student)
    student_dict = {
        "name": student.name,
        "code": student.student_code
    }
    return make_response(student_dict,201)

@app.route('/<name>')
def displayName(name):
    return f'<div>{name}<div>'

@app.before_request
def sayHi():
    print("Hi")

@app.after_request
def sayAfter(something):
    print(something)
    print("after")
    return(something)
# Request Hooks
    # @app.before_request: runs a function before each request.
    # @app.before_first_request: runs a function before the first request (but not subsequent requests).
    # @app.after_request: runs a function after each request.
    # @app.teardown_request: runs a function after each request, even if an error has occurred.
# If we want to run a before request we could save things to g, a global object


# Lets set up out main so we don't have to use flask run
if __name__ == '__main__':
    app.run(port=5555, debug=True)