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
from services import api,app

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)
# db.init_app(app)

# api = Api(app)
# CORS(app)

# app.secret_key = b'D\xf7\xfe,\x06l\xb26\x96\xd4\xe6\xb1\x02m\x13r'
# python -c 'import os; print(os.urandom(16))'

# Storing user specific data
# session['data'] will be different per cookie
# session.get('data') to get the data 
# How can use this for user login?
class handle_session(Resource):
    def get(self):
        print(session)
        print(session.get('test'))
        return {"count":session["count"]},200
    def post(self):
        data = request.get_json()
        session["test"] = data["Test"]
        if not session.get("count"):
            session['count']=0
        session["count"] += 1
        print(session)
        return {"count":session["count"]},200
api.add_resource(handle_session,"/session")
# Lets create a login route that will check if the user exist and
# Save it to session

# Create a logout route now! set session to None

# Use @app.before_request!
class Logout(Resource):
    def delete(self):
        session['user'] = None
        # print(session)
        # Below also works!
        # session.pop('user', None)
        # print(session)
        return {}, 204
api.add_resource(Logout,'/logout')

class Login(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        gotten_user = User.query.filter(User.user_name == data['user_name']).first()
        if gotten_user:
            if gotten_user.authenticate(data['password']):
                if data['stay']:
                    session["user"] = gotten_user.id
                return gotten_user.to_dict(),200
            else:
                return {"Error": "Not valid password"}, 400
        else:
            return {"Error": "Not valid username"}, 400
api.add_resource(Login,'/login')

class Check_Session(Resource):
    def get(self):
        print(session)
        if session.get('user'):
            user = User.query.filter(User.id == session["user"]).first()
            return user.to_dict()
        else:
            return {"session": "user not found"}, 404
api.add_resource(Check_Session, '/check_session')

if __name__ == '__main__':
    app.run(port=5555, debug = True)