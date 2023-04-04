# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py

# Restful

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate


from model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Initialize the Api
api = Api(app)

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)