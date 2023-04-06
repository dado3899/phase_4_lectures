from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# This SerializerMixin import will allow us to call .to_dict()
# on data we query. If we add it to all connected tables
# we could see all the data turned to a dict
# We would need to add a line:
# serialize_rules = ('-tablename.value',)
# This will prevent a loop!
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

# Reminder for foreign keys:
# In sqlalchemy we could have
# many = relationship('many_class', backref='one_tablename')
# one_id = Column(Integer, ForeignKey('one_tablename.id'))

# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

class model():
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)

    # Common additions to most tables to keep track of data! We don't need to add
    # anything when we are creating our seeds
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Nice print'
