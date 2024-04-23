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

from model import db, Teacher

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route("/teachers", methods=['GET','POST'])
def all_teachers():
    if request.method == "GET":
        all_teach = Teacher.query.all()
        r_l = []
        for teach in all_teach:
            r_l.append(teach.to_dict())
        return r_l
    
    elif request.method == "POST":
        # JSON.stringify
        try:
            data = request.get_json()
            t = Teacher(
                name = data["name"],
                email = data["email"],
                specialty = data.get("specialty")
            )
            db.session.add(t)
            db.session.commit()
            return t.to_dict(),201
        except Exception as e:
            print(e)
            return {"Error": "Cannot create teacher"},400

@app.route("/teachers/<int:id>", methods=['GET','PATCH', 'DELETE'])
def one_teacher(id):
    found_teacher = Teacher.query.filter(Teacher.id == id).first()
    if found_teacher:
        teach_in_dict = found_teacher.to_dict(rules=('-lectures.student',))
        u_students = []
        for lecture in found_teacher.lectures:
            student_to_add = lecture.student.to_dict(rules=('-lectures',))
            if student_to_add not in u_students:
                u_students.append(student_to_add)
        teach_in_dict['student'] = u_students
        # return found_teacher.to_dict()
        return teach_in_dict
    else:
        return {"Error": f"Teacher of id {id} does not exist"},400

# Now thinking of paths we can add
# methods=['GET','POST'] to our @app.route('/anything')
# We can then check that request.method == 'GET' or 'POST' and do something accordingly
# For post we can go ahead and use request.form.get("field") or request.get_json()
# EX newcar = Car(make = request.form.get("make"), model=request.form.get("model"))
# We would need to make sure our request has make and model! 
# response = make_response(newcar.to_dict(),201) as an example response
# 201 means a successful post!

# For patch we can use this:
# for attr in request.form:
#     setattr(queried_data, attr, request.form.get(attr))

if __name__ == '__main__':
    app.run(port=5555, debug=True)