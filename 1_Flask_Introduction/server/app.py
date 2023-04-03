# Setting up imports
from flask import Flask, jsonify, make_response, request, g
from flask_migrate import Migrate
from models import db, Vehicle

# Setting up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dmv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
db.init_app(app)

# Now lets run int the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5555
    # flask db init
    # flask db revision --autogenerate -m 'Create tables'
    # flask db upgrade

# Lets create some Seed data!

# We can run the server with flask run and navigate to http://localhost:5555/`
@app.route('/')
def index():
    return f'<div>Hello World</div>'

@app.route('/image')
def image():
    return f'<img src = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTZeekQT0J58IaFG4c3XhsK-AiuSPVzJs3RpK2pwLBeacr6HjNe"/>'

@app.route('/<make>/<model>')
def model_display(make,model):
    new_model = Vehicle.query.filter(db.func.lower(Vehicle.model) == db.func.lower(model), db.func.lower(Vehicle.make) == db.func.lower(make)).first()
    if new_model:
        return f'Hello {g.user} <h1>Model: {new_model.model}, Make: {new_model.make}</h1>'
    else:
        return f'Not a car'
# Routes
    # We can set up routes with @app.route('/')
    # Now lets set up a route that goes to the following image
    # If we have a dynamic route we can use 
        # @app.route('/<title>')
        #  def display(title):
        #     return f'<h1>{title}</h1>'
    # Lets use the class.query.filter() in order to filter like we were using
    # sqlAlchemy
    

# Request Hooks
    # @app.before_request: runs a function before each request.
    # @app.before_first_request: runs a function before the first request (but not subsequent requests).
    # @app.after_request: runs a function after each request.
    # @app.teardown_request: runs a function after each request, even if an error has occurred.
# If we want to run a before request we could save things to g, a global object
@app.before_first_request
def run_before_2():
    print("First")
    

@app.before_request
def run_before():
    g.user = "Test"
    print("Hello")


# Lets set up out main so we don't have to use flask run
if __name__ == '__main__':
    app.run(port=5556, debug=True)