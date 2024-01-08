# Import SQLAlchemy from flask and from sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# This piece of code here i
metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
# This will be our base, we can use our sqlalchemy method of making models using this!
db = SQLAlchemy(metadata=metadata)

# Lets create a class
class NewClass(db.Model):
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)
