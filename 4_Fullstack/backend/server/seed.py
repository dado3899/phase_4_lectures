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
        new_cust = Customer(
            name=faker.name(),
            email = faker.email()
        )
        customers.append(new_cust)
    db.session.add_all(customers)

    print("Seeding Products")
    products = []
    for i in range(50):
        new_product = Product(name=faker.word(),company=faker.word())
        products.append(new_product)
    db.session.add_all(products)

    print("Seeding Orders")
    orders = []
    for i in range(100):
        new_order = Order(
            quantity = randint(1,100),
            price = randint(1,1000),
            product = products[randint(0,len(products)-1)],
            customer = customers[randint(0,len(customers)-1)]
            )
        orders.append(new_order)
    db.session.add_all(orders)
    db.session.commit()