# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup (We added session)
from flask import request, session
from flask_migrate import Migrate
from flask_restful import Resource
from flask_cors import CORS
from models import User
from services import *
import os

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)
# db.init_app(app)

# api = Api(app)
# CORS(app)

# load_dotenv()

#More boilerplate! pipenv install flask_bcrypt
# I would recommend moving that and db into a new file to avoid import errors
# bcrypt = Bcrypt(app)

# print(os.getenv('secret_key'))
# app.secret_key = os.getenv('secret_key')


@app.before_request
def check_credentials():
    valid_routes = ("/check_sessions","/login","/signup")
    # If the route is not in valid routes but the user is logged in 
    if request.path not in valid_routes and 'user_id' not in session:
        return {"error": "please login"},401
    else:
        pass

@app.route('/login', methods = ["POST"])
def login():
    data = request.get_json()
    user = User.query.filter(User.username == data["username"]).first()
    if user:
        if user.check_password(data['password']):
            if data['stayLoggedIn']:
                session["user_id"] = user.id
            return user.to_dict()
        else:
            return {"error":"Not valid password"},400
    else:
        return {"error":"Not valid username"},400

@app.route('/check_sessions')
def check_sessions():
    print(session)
    if session.get("user_id"):
        user = User.query.filter(User.id == session.get("user_id")).first()
        return user.to_dict()
    else:
        return {"error": "no user logged in"},401
    
@app.route('/logout', methods=["DELETE"])
def logout():
    session.pop('user_id')
    return {}, 204

@app.route('/blog/<int:id>')
def get_blog(id):
    if not session.get('reads'):
        session['reads'] = 0
    session['reads'] += 1
    if session['reads'] <= 5:
        return {
            "id": id,
            "data":"This is a blog"
            }
    else:
        return {'error': 'pay me monies'},400
    
@app.route('/signup', methods = ["POST"])
def signup():
    try:
        data = request.get_json()
        user = User(
            username =  data['username'],
            password_hash = data['password']
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict(),201
    except Exception as e:
        print(e)
        return {"error":"cannot create user"},400

@app.route('/change_password',methods=['PATCH'])
def update_password():
    data= request.get_json()
    user = User.query.filter(User.id == data['id']).first()
    if user.check_password(data['existing_password']):
        user.password_hash = data['new_password']
        db.session.add(user)
        db.session.commit()
        return user.to_dict(),200
    else:
        return {'error': 'Not valid existing password'},400


if __name__ == '__main__':
    app.run(port=5555, debug=True)