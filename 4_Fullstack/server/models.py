# imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_`%(constraint_name)s`",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    })

db = SQLAlchemy(metadata=metadata)

class Customer(db.Model,SerializerMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String, unique=True)
    email = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    orders = db.relationship("Order", backref = "customers")
    serialize_rules = ('-orders.customers',)
    @validates('email')
    def check_something(self,key,value):
        if "@" in value:
            return value
        else:
            raise Exception("Not valid email")

    @validates('address','email')
    def check_add(self,key,value):
        if len(value) >= 3:
            return value
        else:
            raise Exception("Not valid Address")

class Product(db.Model,SerializerMixin):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    size = db.Column(db.Integer)
    price = db.Column(db.Float)
    weight = db.Column(db.Float)
    category = db.Column(db.String)
    description = db.Column(db.String)
    # Backref changed to plural to work
    orders = db.relationship("Order", backref = "products")
    serialize_rules = ('-orders.products',)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('category')
    def check_something(self,key,value):
        valid_categories = ["Knives","Forks"]
        if value in valid_categories:
            return value
        else:
            raise Exception("Not valid category")

class Order(db.Model,SerializerMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    serialize_rules = ('-customers.orders','-products.orders')

