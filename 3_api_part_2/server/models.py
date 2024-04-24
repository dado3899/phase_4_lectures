# There are many ways we can add constraints!
# db.CheckConstraint
# nullable = False
# unique = True
# @validates('')

# imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship

metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

db = SQLAlchemy(metadata=metadata)
# Lets do a many to many!
# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

class Country(db.Model,SerializerMixin):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    capital = db.Column(db.String)
    alliances = relationship("Alliance", secondary="treaties",back_populates="countries")
    serialize_rules = ('-alliances.countries',)

    @validates("name")
    def validate_name(self, key, value):
        if 2<=len(value):
            return value
        else:
            raise ValueError("Not valid name")

#To join the two
class Treaty(db.Model,SerializerMixin):
    __tablename__ = 'treaties'
    id = db.Column(db.Integer, primary_key = True)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"))
    alliance_id = db.Column(db.Integer, db.ForeignKey("alliances.id"))
    # country = relationship("Country", back_populates="treaties")
    # alliance = relationship("Alliance", back_populates="treaties")


class Alliance(db.Model,SerializerMixin):
    __tablename__ = 'alliances'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    date = db.Column(db.DateTime)
    countries = relationship("Country", secondary="treaties", cascade='all,delete', back_populates="alliances")
    serialize_rules = ('-countries.alliances',)





