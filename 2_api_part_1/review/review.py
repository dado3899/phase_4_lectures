# Create tables
# Routes
# Before Request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer

metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

db = SQLAlchemy(metadata=metadata)

class Car(db.Model):
    __tablename__ = "Cars"
    id = Column(Integer, primary_key = True)
    make = Column(String, nullable = False)
    model = Column(String, nullable = False)
    year = Column(Integer)

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

# from model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///review.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def index():
    return {"Start": "Here"}, 200

@app.route("/test")
def test():
    return {"Test": "Here"}, 200

@app.route("/cars")
def car_route():
    # db.sesion.query(Car)
    ac = Car.query.all()
    print(ac)
    rl = []
    for car in ac:
        rl.append({"id":car.id,"make":car.make,"model":car.model})
    return rl, 200

# response.ok
@app.route("/cars/<int:id>")
def single_car_route(id):
    sc = Car.query.filter(Car.id == id).first()
    if sc:
        return {"id":sc.id,"make":sc.make,"model":sc.model},200
    else:
        return {"Error": "Not valid car"}, 400

@app.route("/cars/<string:model>/<string:make>")
def car_by_model(model,make):
    ac_by_model  = Car.query.filter(Car.model == model and Car.make==make).all()
    rl = []
    for car in ac_by_model:
        rl.append({"id":car.id,"make":car.make,"model":car.model})
    return make_response(rl,200)
# headers: {application/json}

# Responses
    # by using make_response and jsonify we can make a specific
    # error
# make_response(jsonify(jsonobject),errorcode)
# Common error codes
# 100's - informational
# 200's - success
    # 201 is a success for post!
# 300's - redirect
# 400's - client error
# 500's - server error

# Up next, using postman