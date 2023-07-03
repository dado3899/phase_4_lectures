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
from models import User, Teacher,Student,Schedule

# from flask_bcrypt import Bcrypt
from services import app,bcrypt,db
# Imports for using .env
import os
from dotenv import load_dotenv
# Load the env file
load_dotenv()
# Use os.environ.get() to get the data

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
CORS(app)

app.secret_key = os.environ.get("secretkey")
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
api.add_resource(Login, '/userlogin')

class get_logged_user(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.filter(User.id == session["user_id"]).first()
            res = make_response(jsonify(user.to_dict()),200)
            return res
api.add_resource(get_logged_user, '/logged_user')

class check_logged_in(Resource):
    def get(self):
        print(session)
        user_id = session.get('user_id')
        if user_id:
            if user_id != None:
                return make_response({"logged_in": True},200)
        return make_response({"logged_in": False},200)
api.add_resource(check_logged_in,'/check')

class logout(Resource):
    def delete(self):
        session['user_id'] = None
        res = make_response(jsonify({ "login" : "Logged out"}),200)
        return res
api.add_resource(logout, '/logout')

class get_type(Resource):
    def get(self):
        if session.get("valid"):
            game = Game.query.filter(Game.id == session["game_id"]).first()
            playerA = Player.query.filter(Player.id==game.playerA).first
            user = User.query.filter(User.id == session["user_id"]).first() 
            res = make_response(jsonify({ "user_type" : user.user_type}),200)
            return res
        else:
            res = make_response(jsonify({ "login" : "invalid user"}),400)
            return res
api.add_resource(get_type, '/get_type')

class delete_teach(Resource):
    def get(self,id):
        teach = Teacher.query.filter(Teacher.id == id).first()
        return make_response(teach.to_dict(),200)
    def delete(self,id):
        teach = Teacher.query.filter(Teacher.id == id).first()
        db.session.delete(teach)
        db.session.commit()
        return make_response({},200)
api.add_resource(delete_teach, '/teacher/<id>')

class delete_student(Resource):
    def get(self,id):
        teach = Student.query.filter(Student.id == id).first()
        return make_response(teach.to_dict(),200)
    def delete(self,id):
        teach = Student.query.filter(Student.id == id).first()
        db.session.delete(teach)
        db.session.commit()
        return make_response({},200)
api.add_resource(delete_student, '/student/<id>')

# @app.before_request
# def validate():
#     if session.get("user_id"):
#         user = User.query.filter(User.id == session["user_id"]).first()
#         if user.user_type == 'Zebra':
#             session["valid"] = True
#         else:
#             session["valid"] = False
#     else:
#         session["valid"] = False

if __name__ == '__main__':
    app.run(port=5555)