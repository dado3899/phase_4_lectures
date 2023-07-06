# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup (We added session)
# Yay more boiler plate!
from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import User
from services import db,app,api

# python -c 'import os; print(os.urandom(16))'

# Use @app.before_request!
@app.before_request
def checkUser():
    data = session.get('data')
    current_user_id = session.get('user_id')
    print(request.endpoint)
    bypassroutes = ["loginmethod"]
    if request.endpoint not in bypassroutes:
        if current_user_id:
            print(User.query.filter(User.id == current_user_id).first().to_dict())
        else:
            return make_response({"Status": "Not logged in"},400)

class All_Customers(Resource):
    def get(self):
        json_obj = { "Type" : "Get"}
        print(session.get('data'))
        print(session)
        # count = session.get('pageCount')
        # session['pageCount'] += 1
        res = make_response(jsonify(json_obj),200)
        return res

    def post(self):
        json_obj = { "Type" : "Post"}
        response = request.get_json()
        print(response["data"])
        session['data'] = response["data"]
        res = make_response(jsonify(json_obj),200)
        return res
api.add_resource(All_Customers, '/students')

class loginMethod(Resource):
    def post(self):
        response = request.get_json()
        current_user = User.query.filter(User.user == response["user"]).first()
        print(type(current_user))
        if current_user and current_user.authenticate(response['password']):
            session["user_id"] = current_user.id
            return make_response(current_user.to_dict(),200)
        else:
            return make_response({"Status":"Invalid credentials"},400)
api.add_resource(loginMethod, '/login')

class logoutMethod(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({"Logout": "Success"}, 200)
api.add_resource(logoutMethod, '/logout')


if __name__ == '__main__':
    app.run(port=5555)