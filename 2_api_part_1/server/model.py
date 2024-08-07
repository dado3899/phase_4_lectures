from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship
# This SerializerMixin import will allow us to call .to_dict()
# on data we query. If we add it to all connected tables
# we could see all the data turned to a dict
# We would need to add a line:
# serialize_rules = ('-tablename.value',)
# This will prevent a loop!
from sqlalchemy_serializer import SerializerMixin
metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
db = SQLAlchemy(metadata=metadata)

# Reminder for foreign keys:
# In sqlalchemy we could have
# many = relationship('many_class', backref='one_tablename')
# one_id = Column(Integer, ForeignKey('one_tablename.id'))

# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

class Chef(db.Model,SerializerMixin):
    __tablename__ = 'chefs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    specialty = db.Column(db.String)
    phone = db.Column(db.String)
    pastries = relationship("Pastry", back_populates="chef")
    # serialize_only = ("name","id")
    serialize_rules = ('-pastries.chef','-created_at','-updated_at')

    # Common additions to most tables to keep track of data! We don't need to add
    # anything when we are creating our seeds
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class Pastry(db.Model,SerializerMixin):
    __tablename__ = "pastries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    moisture_content = db.Column(db.Integer)
    country_of_origin = db.Column(db.String)
    chef_id = db.Column(db.Integer, db.ForeignKey("chefs.id"))

    chef = relationship("Chef", back_populates="pastries")

    serialize_rules = ('-chef.pastries',)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
