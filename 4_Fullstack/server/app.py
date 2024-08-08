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
        all_cust = Customer.query.all()
        return [cust.to_dict() for cust in all_cust]
    def post(self):
        try:
            data = request.get_json()
            customer = Customer(
                name = data['name'],
                email = data['email'],
                secondary_email = data.get('email2')
            )
            db.session.add(customer)
            db.session.commit()
            return customer.to_dict(),201
        except Exception as e:
            print(e)
            return {
                "error": "Validation Error"
            },400
api.add_resource(All_Customers, '/customers')

class One_Customer(Resource):
    def get(self,id):
        cust = Customer.query.filter(Customer.id == id)
        if cust:
            return cust.to_dict()
        else:
            return {"error":"not valid id"},400
    def patch(self,id):
        cust = Customer.query.filter(Customer.id == id)
        if cust:
            try:
                data = request.get_json()
                for key in data:
                    setattr(cust,key,data[key])
                db.session.add(cust)
                db.session.commit()
            except Exception as e:
                print(e)
                return {
                    "error": "Validation Error"
                }
        else:
            return {"error":"not valid id"},400
    def delete(self,id):
        cust = Customer.query.filter(Customer.id == id).first()
        if cust:
            # ao = Order.query.filter(Order.customer_id==id).all()
            # for o in ao:
            #     db.session.delete(o)
            db.session.delete(cust)
            db.session.commit()
            return {}
        else:
            return {"error":"not valid id"},400
api.add_resource(One_Customer,'/customers/<int:id>')

class Login(Resource):
    def post(self):
        data = request.get_json()
        cust = Customer.query.filter(Customer.email == data['email']).first()
        if cust:
            return cust.to_dict()
        else:
            return {
                "error": "Invalid Credentials"
            },400

api.add_resource(Login,'/login')
if __name__ == '__main__':
    app.run(port=5555,debug=True)