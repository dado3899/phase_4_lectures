# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db migrate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup (We added session)
from flask import request, session
from flask_restful import Resource
from flask_cors import CORS
from models import User,db
from flask_bcrypt import Bcrypt
from services import api,app


# Storing user specific data
# session['data'] will be different per cookie
# session.get('data') to get the data 
class SaveSession(Resource):
    def get(self):
        print(session)
        return {}
    def post(self):
        data = request.get_json()
        session['data'] = data['data']
        print(data)
        return {}

api.add_resource(SaveSession,'/session')

# How can use this for user login?

# Lets create a login route that will check if the user exist and
# Save it to session
class Login(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        user = User.query.filter(User.username == data['username']).first()
        if user and user.authenticate(data['password']):
            if data['stayLoggedIn']:
                session['user_id'] = user.id
            return user.to_dict()
        else:
            return {"Error": "Not valid user"},400
api.add_resource(Login,'/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}
api.add_resource(Logout,'/logout')

class Signup(Resource):
    def post(self):
        try:
            data = request.get_json()
            user = User( username = data['username'], password_hash = data['password'])
            print(user.username)
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return user.to_dict()
        except Exception as e:
            print(e)
            return {"Error":"Can't signup"},400
api.add_resource(Signup,'/signup')

class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session.get('user_id')).first()
            return user.to_dict()
        else:
            return {},404
api.add_resource(CheckSession,'/checksessions')
# Create a logout route now! set session to None


# Use @app.before_request!
@app.before_request
def check_session():
    valid_routes = ['/checksessions','/login','/signup']
    # print(request.path)
    if session.get('user_id') or request.path in valid_routes:
        pass
    else:
        return {
            "error":"not valid route"
        },400

class All_Items(Resource):
    def get(self):
        json_obj = { "Type" : "Get"}
        res = {"data":"Sesnsative Data"},200
        return res

api.add_resource(All_Items, '/items')

if __name__ == '__main__':
    app.run(port=5555, debug=True)