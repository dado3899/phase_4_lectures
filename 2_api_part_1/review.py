from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# Create tables
metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
db = SQLAlchemy(metadata=metadata)
class Computer(db.Model):
    __tablename__ = "computers"
    id = db.Column(db.Integer, primary_key=True)
    gpu = db.Column(db.String)
    

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db,Computer

# Setting up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
db.init_app(app)

@app.route("/test")
def test():
    print("Test")
    return {}

@app.route("/<float:whatever>")
def test2(whatever):
    print(whatever)
    return {},200
# Routes
# Before Request

# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#using-custom-metadata-and-naming-conventions
# https://alembic.sqlalchemy.org/en/latest/naming.html#the-importance-of-naming-constraints

# db = SQLAlchemy(metadata=metadata)

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