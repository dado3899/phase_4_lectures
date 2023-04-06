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

# Option 1 for routes
class All_Customers(Resource):
    def get(self):
        print("restful")
        all_cust = Customer.query.all()
        all_customer = []
        for cust in all_cust:
            all_customer.append(cust.to_dict())
        res = make_response(jsonify(all_customer),200)
        return res

    def post(self):
        jsoned_request = request.get_json()
        print(jsoned_request)
        new_customer = Customer(
            name=jsoned_request['name'],
            address = jsoned_request['address'],
            email = jsoned_request['email'],
            age = jsoned_request['age']
        )
        db.session.add(new_customer)
        db.session.commit()
        res = make_response(jsonify(new_customer.to_dict()),200)
        return res
api.add_resource(All_Customers, '/customers')

# Option 2 for routes
@app.route('/products', methods = ['GET','POST'])
def get_products():
    print("App route")
    if request.method == 'GET':
        all_prod = Product.query.all()
        all_products = []
        for prod in all_prod:
            all_products.append(prod.to_dict())
        res = make_response(jsonify(all_products),200)
        return res

if __name__ == '__main__':
    app.run(port=5555)
