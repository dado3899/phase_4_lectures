# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Customer,Product,Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
# New addition to aid in cors errors
CORS(app)

class All_Customers(Resource):
    def get(self):
        customers = Customer.query.all()
        cust_dict = []
        for customer in customers:
            cust_dict.append(customer.to_dict())
        return cust_dict,200
        # return [customer.to_dict() for customer in customers],200

    def post(self):
        try:
            data = request.get_json()
            new_cust = Customer(
                name = data["name"],
                email = data["email"]
            )
            db.session.add(new_cust)
            db.session.commit()
            return new_cust.to_dict(),201
        except Exception as e:
            print(e)
            return {"Error": "Not valid data"},400


class One_Customer(Resource):
    # def get_one(self):
    #     found_customer = Customer.query.filter(Customer.id == id).first()
    #     if found_customer:
    #         return found_customer
    #     else:
    #         return {"Error": f"Customer id {id} cannot be found"}
    def get(self,id):
        found_customer = Customer.query.filter(Customer.id == id).first()
        if found_customer:
            return found_customer.to_dict(),200
        else:
            return {"Error": f"Customer id {id} cannot be found"}
    def patch(self,id):
        found_customer = Customer.query.filter(Customer.id == id).first()
        if found_customer:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(found_customer,attr,data[attr])
                db.session.add(found_customer)
                db.session.commit()
                return found_customer.to_dict(),200
            except Exception as e:
                print(e)
                return {"Error": "Failed patch"},400
        else:
            return {"Error": f"Customer id {id} cannot be found"}
    def delete(self,id):
        found_customer = Customer.query.filter(Customer.id == id).first()
        if found_customer:
            try:
                db.session.delete(found_customer)
                db.session.commit()
                return {"Status": "Deleted"}, 200
            except:
                return {"Error": "Failed to delete"},400
        else:
            return {"Error": f"Customer id {id} cannot be found"},400

# custprod
class Add_Product_to_Customer(Resource):
    def post(self):
        data = request.get_json()
        # Given a customer
        # Check if that customer exists
        customer = Customer.query.filter(Customer.id == data["cust_id"]).first()
        if customer:
        # Check if product exists by name and company
        # If not create product
        # if so continue
        # Create an order
            product = Product.query.filter(Product.name == data["name"] and Product.company==data["company"]).first()
            if not product:
                product = Product(
                    name = data["name"],
                    company = data["company"]
                )
                db.session.add(product)
            order = Order(
                quantity = data["quantity"],
                price = data["price"],
                product = product,
                customer = customer
            )
            db.session.add(order)
            db.session.commit()

            return order.to_dict(), 201
        else:
            return {"ERROR":"Not valid customer"},400
api.add_resource(All_Customers, '/customers')
api.add_resource(One_Customer,'/customers/<int:id>')
api.add_resource(Add_Product_to_Customer,'/custprod')

if __name__ == '__main__':
    app.run(port=5555,debug = True)