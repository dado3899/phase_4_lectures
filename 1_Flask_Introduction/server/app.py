# Setting up imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db, Yoyo

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
    # flask db migrate -m 'Create tables productions'
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
@app.before_first_request
def before_first_r():
    print("REAL FIRST")

@app.before_request
def before_request():
    not_logged_in_routes = ('/login','/signup','/')
    print("THIS IS BEFORE THE ROUTE")
    valid_apis = (123,124,125)
    # Get apikey from frontend
    # request.path to get path
    apikey = 123
    if apikey in valid_apis:
        pass
    else:
        return {"Error":"Please put valid api key"}


@app.route('/')
def display_default():
    return '<h1>Welcome</h1>'

# @app.route('/<title>/<author>')
# def display_title(title,author):
#     print(title,author)
#     return f'<h1>{title}</h1>'

@app.route('/yoyos')
def yoyo():
    all_yoyos = Yoyo.query.all()
    return [{
        "id":yoyo.id,
        "rpm": yoyo.rpm,
        "company": yoyo.company,
        "size": yoyo.size
        } for yoyo in all_yoyos
        ]

@app.route('/yoyos/<int:id>')
def one_yoyo(id):
    one_yoyo = Yoyo.query.filter(Yoyo.id == id).first()
    print(one_yoyo)
    if one_yoyo:
        return {
            "id":one_yoyo.id,
            "rpm": one_yoyo.rpm,
            "company": one_yoyo.company,
            "size": one_yoyo.size
            }
    else:
        raise ValueError("Not valid yoyo id")
        return {
            "error": "Not valid Yoyo id"
        }, 400

@app.after_request
def after(r):
    print("Trigger after")
    return r
@app.teardown_request
def after_w_err(r):
    print("teardown")
    print(r)
# Request Hooks
    # @app.before_request: runs a function before each request.
    # @app.before_first_request: runs a function before the first request (but not subsequent requests).
    # @app.after_request: runs a function after each request.
    # @app.teardown_request: runs a function after each request, even if an error has occurred.


# Lets set up out main so we don't have to use flask run
if __name__ == '__main__':
    app.run(port=5555, debug=True)