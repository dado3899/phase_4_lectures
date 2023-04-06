from app import app 
from models import db, Customer,Product,Order
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    Customer.query.delete()
    print("Deleting Products")
    Product.query.delete()
    print("Deleting Orders")
    Order.query.delete()
    print("Seeding Customers")
    customers = []
    for i in range(50):
        new_cust = Customer(name=faker.name())
        customers.append(new_cust)
    db.session.add_all(customers)

    print("Seeding Teachers")
    products = []
    for i in range(50):
        new_product = Product(name=faker.word())
        products.append(new_product)
    db.session.add_all(products)

    print("Seeding Orders")
    orders = []
    for i in range(50):
        new_schedule = Order(
            name = ""
            )
    db.session.add_all(orders)
    db.session.commit()