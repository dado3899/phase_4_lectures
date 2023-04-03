# Setting up imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db

# Setting up the app
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# migrate = Migrate(app,db)
# db.init_app()

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
    

# Request Hooks
    # @app.before_request: runs a function before each request.
    # @app.before_first_request: runs a function before the first request (but not subsequent requests).
    # @app.after_request: runs a function after each request.
    # @app.teardown_request: runs a function after each request, even if an error has occurred.
# If we want to run a before request we could save things to g, a global object


# Lets set up out main so we don't have to use flask run
# if __name__ == '__main__':
#     app.run(port=5555, debug=True)