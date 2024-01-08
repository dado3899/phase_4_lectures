# Setting up imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db, Pet

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


@app.route('/specific')
def home_route():
    raise Exception("Not happy")
    return f'<h1>Hello<h1>'

@app.route('/test/<string:id>')
def dynamic_test(id):
    print(type(id))
    return {"test":id}

@app.route('/<title>')
def dynamic_display(title):
    print(title)
    return {"Data":title}

@app.route('/test')
def test_route():
    return {"Data":"test"}

# @app.route('/test2')
# def test2_route():

@app.route('/pets')
def show_pets():
    all_pets = Pet.query.all()
    print(all_pets)
    r_arr = []
    for pet in all_pets:
        pet_dict = {
            "id":pet.id,
            "name":pet.name,
            "age":pet.age,
            "species": pet.species
        }
        r_arr.append(pet_dict)
    return r_arr
@app.route('/pets/<int:id>')
def get_one_pet(id):
    one_pet = Pet.query.filter(Pet.id==id).first()
    print(one_pet)
    if one_pet:
        pet_dict = {
            "id":one_pet.id,
            "name":one_pet.name,
            "age":one_pet.age,
            "species": one_pet.species
        }
        return pet_dict
    else:
        return {"Error": "Not valid id"}, 400

@app.before_request
def check_something():
    print("Before request here")
    # if(user not logged in)
    #     return {"Error": "NEED TO LOGIN"}

# @app.before_first_request
# def bfr():
#     print("Before first request")

# @app.after_request
# def after(something):
#     print(something)
#     print("After")
#     return something

# @app.teardown_request
# def teardown(something):
#     print("teardown")
#     return something

# Request Hooks
    # @app.before_request: runs a function before each request.
    # @app.before_first_request: runs a function before the first request (but not subsequent requests).
    # @app.after_request: runs a function after each request.
    # @app.teardown_request: runs a function after each request, even if an error has occurred.
# If we want to run a before request we could save things to g, a global object


# Lets set up out main so we don't have to use flask run
if __name__ == '__main__':
    app.run(port=5555, debug=True)