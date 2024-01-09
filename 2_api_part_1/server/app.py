# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # (Build models here)
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

from model import db, Teacher, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/teachers', methods = ['GET','POST'])
def teacher_route():
    print(request.method)
    if request.method == 'GET':
        teachers_obj = Teacher.query.all()
        teachers_dict = []
        print(teachers_obj)
        for teacher in teachers_obj:
            teachers_dict.append(teacher.to_dict())
        return teachers_dict,200
    elif request.method == 'POST':
        json_dict = request.get_json()
        new_teach = Teacher(
            name = json_dict.get("name"),
            email = json_dict.get("email")
        )
        db.session.add(new_teach)
        db.session.commit()
        return new_teach.to_dict(),201
    
@app.route('/teachers/<int:id>', methods = ['GET','POST','PATCH','DELETE'])
def single_teacher_route(id):
    teacher = Teacher.query.filter(Teacher.id == id).first()
    if teacher:
        if request.method == 'GET':
            return teacher.to_dict(),200
        elif request.method == 'POST':
            json_dict = request.get_json()
            ns = Student(
                name = json_dict.get("name"),
                email = json_dict.get("email"),
                teacher_id = teacher.id
            )
            db.session.add(ns)
            db.session.commit()
            return teacher.to_dict(), 201
        elif request.method == 'PATCH':
            json_dict = request.get_json()
            for attr in json_dict:
                setattr(teacher, attr, json_dict.get(attr))
            db.session.add(teacher)
            db.session.commit()
            return teacher.to_dict(),201
        elif request.method == "DELETE":
            for stud in teacher.students:
                db.session.delete(stud)
            db.session.delete(teacher)
            db.session.commit()
            return {"Success": True}, 200
    else:
        return {"Error":"Teacher not found"},400

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