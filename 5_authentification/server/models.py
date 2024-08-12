# imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

from services import bcrypt,db

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    _password_hash = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    # Now we create a setter function!
    @password_hash.setter
    def password_hash(self, password):
        #NOTE WE NEED THE ENCODE AND DECODE IN PYTHON 3 DUE TO SPECIAL CHARACTERS ∫ ß å
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))
