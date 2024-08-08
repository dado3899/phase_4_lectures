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
        new_cust = Customer(name=faker.name(), email=faker.email(), secondary_email=faker.email())
        customers.append(new_cust)
    db.session.add_all(customers)
    db.session.commit()

    print("Seeding Products")
    products = []
    for i in range(50):
        new_product = Product(name=faker.word(),company=faker.word()+" inc", inventory=randint(1,100),cost=randint(1,100))
        products.append(new_product)
    db.session.add_all(products)
    db.session.commit()

    print("Seeding Orders")
    orders = []
    delivery_options = ["shipping","delivered","in warehouse","lost"]
    for cust in customers:
        for i in range(5):
            new_order = Order(
                    discount_percentage = 0,
                    delivery_status = delivery_options[randint(0,3)],
                    customer = cust,
                    product = products[randint(0,49)]
                )
            orders.append(new_order)
    db.session.add_all(orders)
    db.session.commit()