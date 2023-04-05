from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# This SerializerMixin import will allow us to call .to_dict()
# on data we query. If we add it to all connected tables
# we could see all the data turned to a dict
# We would need to add a line:
# serialize_rules = ('-tablename.value',)
# This will prevent a loop!
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import MetaData

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

# join = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# join = relationship('Join_class', backref='many1')
class Person(db.Model,SerializerMixin):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    vehicles = db.relationship('Vehicle', backref='persons')
    serialize_rules = ('-vehicles.persons',)
    # Common additions to most tables to keep track of data! We don't need to add
    # anything when we are creating our seeds
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    

    def __repr__(self):
        return f'Person: {self.name}'

class Vehicle(db.Model,SerializerMixin):
    __tablename__ = 'vehicles'
    serialize_rules = ('-persons.vehicles',)
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    registered = db.Column(db.Boolean)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'''
        Make: {self.make}
        Model: {self.model}
        Year: {self.year}
        '''

