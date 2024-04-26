# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup (We added session)
from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, User
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
CORS(app)

load_dotenv()
app.secret_key = os.getenv('secret_key')
# python -c 'import os; print(os.urandom(16))'
# Lets use a .env file!
# pipenv install python-dotenv
# from dotenv import load_dotenv
# os.getenv("MY_KEY")

# Storing user specific data
# session['data'] will be different per cookie
# session.get('data') to get the data 
# How can use this for user login?

@app.route('/login', methods = ["POST"])
def login():
    data = request.get_json()
    user = User.query.filter(User.username == data["username"]).first()
    if user:
        session["user_id"] = user.id
        return user.to_dict()
    else:
        return {"error":"Cannot login"},400

@app.route('/check_sessions')
def check_sessions():
    if session.get("user_id"):
        user = User.query.filter(User.id == session.get("user_id")).first()
        return user.to_dict()
    else:
        return {"error": "no user logged in"},401


# Lets create a login route that will check if the user exist and
# Save it to session

# Create a logout route now! set session to None

# Use @app.before_request!

class All_Customers(Resource):
    def get(self):
        json_obj = { "Type" : "Get"}
        res = make_response(jsonify(json_obj),200)
        return res

    def post(self):
        json_obj = { "Type" : "Post"}
        res = make_response(jsonify(json_obj),200)
        return res
api.add_resource(All_Customers, '/students')

if __name__ == '__main__':
    app.run(port=5555, debug=True)