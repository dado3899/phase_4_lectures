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
from sqlalchemy.orm import relationship

metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

db = SQLAlchemy(metadata=metadata)
# Lets do a many to many!
# many1 = relationship('Many2',secondary = "join_table" backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Many1',secondary = "join_table" backref='many1')

class Chef(db.Model,SerializerMixin):
    __tablename__ = 'chefs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)
    phone = db.Column(db.String,unique=True)
    pastries = relationship("Pastry",secondary="recipes",back_populates = "chefs")
    # serialize_only = ("name","id")
    serialize_rules = ('-pastries.chefs','-created_at','-updated_at')

    # Common additions to most tables to keep track of data! We don't need to add
    # anything when we are creating our seeds
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class Recipe(db.Model,SerializerMixin):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    chef_id = db.Column(db.Integer,db.ForeignKey("chefs.id"))
    pastry_id = db.Column(db.Integer,db.ForeignKey("pastries.id"))

class Pastry(db.Model,SerializerMixin):
    __tablename__ = "pastries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    moisture_content = db.Column(db.Integer)
    country_of_origin = db.Column(db.String)
    chefs = relationship("Chef",secondary="recipes",back_populates = "pastries")

    @validates("moisture_content")
    def validate_moisture(self,key,value):
        if type(value) is int and 0<=(value)<=100:
            return value
        else:
            raise ValueError("Not valid moisture content")
        
    @validates("name","country_of_origin")
    def validate_two(self,key,value):
        if type(value) is str:
            if key == "name" and 1<len(value):
                return value
            elif key == "country_of_origin" and 2<len(value)<=10:
                return value
        raise ValueError(f"not valid {key}")
        

    ingredients = relationship("Ingredient", back_populates="pastry")

    serialize_rules = ('-ingredients.pastry','-chefs.pastries')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
class Ingredient(db.Model,SerializerMixin):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    amount = db.Column(db.Integer)
    measurement_type = db.Column(db.String)

    pastry_id = db.Column(db.Integer,db.ForeignKey("pastries.id"))
    pastry = relationship("Pastry", back_populates="ingredients")
    serialize_rules = ("-pastry.ingredients",)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())