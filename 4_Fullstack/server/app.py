# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Customer,Product,Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
# New addition to aid in cors errors
CORS(app)

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
    app.run(port=5555)