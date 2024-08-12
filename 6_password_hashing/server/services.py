from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

# Move Boilerplate in here!

# creating a bcrypt
# bcrypt = Bcrypt(app)