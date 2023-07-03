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
from models import User

# Yay more boiler plate!
from flask_bcrypt import Bcrypt
from services import app,bcrypt,db
# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
CORS(app)
# creating a bcrypt
# bcrypt = Bcrypt(app)

# After setting up the bcrypt in our models we can go ahead and create a 
# sign up route as well as edit our login route
# to use our authenticate
# Use the following as a catch all for errors!
# try:
#   something
# except:
#   abort(401, "Unauthorized")

app.secret_key = b'\xcd\x9f.\xe9n\x18\x1c\x8f\xeby\xbf#\xaf\xa8z{'
# python -c 'import os; print(os.urandom(16))'
class CreateUser(Resource):
    def post(self):
        jsoned_request = request.get_json()
        new_user = User(name = jsoned_request["name"],user_type = jsoned_request["user_type"])
        new_user.password_hash = jsoned_request["password"]
        db.session.add(new_user)
        db.session.commit()
api.add_resource(CreateUser, '/signup')

class Login(Resource):
    def post(self):
        jsoned_request = request.get_json()
        user = User.query.filter(User.name == jsoned_request["name"]).first()
        if user.authenticate(jsoned_request["password"]):
            session['user_id'] = user.id
            res = make_response(jsonify(user.to_dict()),200)
            return res
        else:
            res = make_response(jsonify({ "login" : "Invalid User"}),500)
            return res    
api.add_resource(Login, '/login')
class check_login(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.filter(User.id == session["user_id"]).first()
            res = make_response(jsonify(user.to_dict()),200)
            return res
api.add_resource(check_login, '/checklogin')

class logout(Resource):
    def delete(self):
        session['user_id'] = None
        res = make_response(jsonify({ "login" : "Logged out"}),200)
        return res
api.add_resource(logout, '/logout')

class get_type(Resource):
    def get(self):
        if session.get("valid"):
            user = User.query.filter(User.id == session["user_id"]).first() 
            res = make_response(jsonify({ "user_type" : user.user_type}),200)
            return res
        else:
            res = make_response(jsonify({ "login" : "invalid user"}),400)
            return res
api.add_resource(get_type, '/get_type')

@app.before_request
def validate():
    if "user_id" in session:
        user = User.query.filter(User.id == session["user_id"]).first()
        if user.user_type == 'Zebra':
            session["valid"] = True
        else:
            session["valid"] = False
    else:
        session["valid"] = False

if __name__ == '__main__':
    app.run(port=5555)