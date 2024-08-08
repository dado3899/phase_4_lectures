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

class Customer(db.Model,SerializerMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True)
    secondary_email = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = relationship('Order', back_populates='customer', cascade="all, delete-orphan")

    serialize_rules = ('-orders.customer',)
    @validates('email','secondary_email')
    def validate_email(self,key,value):
        if (type(value) is str and "@" in value and "." in value) or (key=="secondary_email" and value==None):
            return value
        else:
            raise ValueError("Not valid email")

class Product(db.Model,SerializerMixin):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    company = db.Column(db.String)
    inventory = db.Column(db.String)
    cost = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = relationship('Order', back_populates='product', cascade="all, delete-orphan")
    serialize_rules = ('-orders.product',)

class Order(db.Model,SerializerMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    discount_percentage = db.Column(db.Float)
    delivery_status = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id')) 
    customer = relationship('Customer', back_populates='orders')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = relationship('Product', back_populates='orders')   

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-customer.orders','-product.orders')

    @validates('discount_percentage')
    def validate_dp(self,key,value):
        if 0<=value<=1:
            return value
        else:
            raise ValueError("Not valid percentage")