# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
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

from model import db,Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Now thinking of paths we can add
# methods=['GET','POST'] to our @app.route('/anything')
# We can then check that request.method == 'GET' or 'POST' and do something accordingly
# For post we can go ahead and use request.form.get("field")
# EX newcar = Car(make = request.form.get("make"), model=request.form.get("model"))
# We would need to make sure our request has make and model! 
# response = make_response(newcar.to_dict(),201) as an example response
# 201 means a successful post!

@app.route('/students',methods=['GET','POST'])
def displayStudents():
    method = request.method
    if method == "GET":
        students = Student.query.all()
        all_students = []
        for student in students:
            all_students.append(student.to_dict())
        return make_response(all_students,200)
    elif method == "POST":
        request_data = request.get_json()
        new_student = Student(
            name = request_data["name"], 
            student_code =request_data["student_code"],
            school = request_data["school"]
            )
        db.session.add(new_student)
        db.session.commit()
        return make_response(new_student.to_dict(),201)
    return {}

@app.route('/students/<id>',methods=['GET','PATCH','DELETE'])
def displayOneStudents(id):
    method = request.method
    student = Student.query.filter(Student.id == id).first()
    if student:
        if method == "PATCH":
            request_data = request.get_json()
            for attr in request_data:
                setattr(student,attr,request_data[attr])
            print(student.to_dict())
            db.session.add(student)
            db.session.commit()
            return make_response(student.to_dict(),200)
        elif method == "DELETE":
            db.session.delete(student)
            db.session.commit()
            return make_response({"Deleted":True},200)
    else:
        return make_response({"Student": None}, 400)
# For patch we can use this:
# for attr in request.form:
#     setattr(queried_data, attr, request.form.get(attr))

if __name__ == '__main__':
    app.run(port=5555)