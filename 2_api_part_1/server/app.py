# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # flask db init
        # flask db migrate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /model       	| READ all resources 	|
# | GET       	| /model/:id    	| READ one resource   	|
# | POST      	|   /model      	| CREATE one resource 	|
# | PATCH/PUT 	| /model/:id    	| UPDATE one resource	|
# | DELETE    	| /model/:id    	| DESTROY one resource 	|

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

from model import db, Chef, Pastry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/chefs",methods=["GET","POST"])
def chefs_route():
    print(request.method)
    if request.method=="GET":
        all_cs = Chef.query.all()
        r_list = []
        for chef in all_cs:
            r_list.append(chef.to_dict())
        return r_list,200
    elif request.method=="POST":
        #Do the post
        try:
            data = request.get_json()
            new_chef = Chef(
                name = data["name"],
                specialty = data["specialty"],
                phone=data["phone"]
            )
            db.session.add(new_chef)
            db.session.commit()
            return new_chef.to_dict(),201
        except Exception as e:
            print(e)
            return {
                "Error": "Please input all values"
            },400

@app.route("/chefs/<int:id>")
def one_chef_route(id):
    print(request.method)
    chef = Chef.query.filter(Chef.id == id).first()
    # chef.to_dict(rules=('-phone',))
    # chef.to_dict(only=("name",))
    if chef:
        return chef.to_dict(), 200
    else:
        return {
            "Error": f"{id}: Not valid id"
        }, 400
    


# Now thinking of paths we can add
# methods=['GET','POST'] to our @app.route('/anything')
# We can then check that request.method == 'GET' or 'POST' and do something accordingly
# For post we can go ahead and use request.form.get("field")
# EX newcar = Car(make = request.form.get("make"), model=request.form.get("model"))
# We would need to make sure our request has make and model! 
# response = make_response(newcar.to_dict(),201) as an example response
# 201 means a successful post!

# For patch we can use this:
# for attr in request.form:
#     setattr(queried_data, attr, request.form.get(attr))

if __name__ == '__main__':
    app.run(port=5555, debug=True)