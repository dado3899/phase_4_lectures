# request.get_json()
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class All_Customers(Resource):
    def get(self):
        ac = Customer.query.all()
        return [customer.to_dict() for customer in ac]
    def post(self):
        try:
            data = request.get_json()
            c = Customer(
                name = data["name"],
                email = data["email"]
            )
            db.session.add(c)
            db.session.commit()
            return c.to_dict(),201
        except Exception as e:
            print(e)
            return {"Error": "Not valid customer, please edit data"}, 400
api.add_resource(All_Customers,'/customers')

class One_Customer(Resource):
    def get(self,id):
        cust = Customer.query.filter(Customer.id == id).first()
        if cust:
            return cust.to_dict()
        else:
            return {"Error": "Not valid id"},404
    def patch(self,id):
        cust = Customer.query.filter(Customer.id == id).first()
        if cust:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(cust,attr,data[attr])
                db.session.add(cust)
                db.session.commit()
                return cust.to_dict()
            except Exception as e:
                return {"Error":"Cannot update customer"},400
        else:
            return {"Error": "Not valid id"},404
    def delete(self,id):
        cust = Customer.query.filter(Customer.id == id).first()
        if cust:
            db.session.delete(cust)
            db.session.commit()
            return {}, 204
        else:
            return {"Error": "Not valid id"},404
api.add_resource(One_Customer,'/customers/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug = True)
