# imports
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from services import *

#More boilerplate! We need to import THE SAME bcrypt we created in app
# I would recommend moving that and db into a new file to avoid import errors
# metadata = MetaData(naming_convention={
#     "ix": "ix_%(column_0_label)s",
#     "uq": "uq_%(table_name)s_%(column_0_name)s",
#     "ck": "ck_%(table_name)s_`%(constraint_name)s`",
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#     "pk": "pk_%(table_name)s"
#     })

# db = SQLAlchemy(metadata=metadata)

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    _password_hash = db.Column(db.String)
    # we need to create a _password_hash = db.Column(db.String)
    # password hashes=> adfsbhiafdbohafhjlafbhoaf 
    # adfsbhiafdbohafhjlafbhoaf =/= password

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-_password_hash',)

     #next create a hybrid property, its similar to a regular property
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    # Now we create a setter function!
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
        # NOTE WE NEED THE ENCODE AND DECODE IN PYTHON 3 DUE TO SPECIAL CHARACTERS ∫ ß å

    # Now lets create an authentification route using
    # bcrypt.check_password_hash(_password_hash, password.encode('utf-8'))
    def check_password(self,password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))