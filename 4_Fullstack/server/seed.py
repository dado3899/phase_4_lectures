from app import app 
from models import db, Customer,Product,Order
from faker import Faker
from random import randint
import datetime
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
        new_cust = Customer(
            name=faker.name(),
            email=faker.email()
        )
        customers.append(new_cust)
    db.session.add_all(customers)

    print("Seeding Product")
    products = []
    for i in range(50):
        new_product = Product(name=faker.word(), company=faker.word()+" Inc")
        products.append(new_product)
    db.session.add_all(products)

    print("Seeding Orders")
    orders = []
    for i in range(50):
        new_order = Order(
                customer = customers[randint(0,len(customers)-1)],
                product = products[randint(0,len(products)-1)],
                date = datetime.datetime.strptime(faker.date(), '%Y-%m-%d').date(),
                price = randint(0,100)+ 0.99
            )
        orders.append(new_order)
    db.session.add_all(orders)
    db.session.commit()