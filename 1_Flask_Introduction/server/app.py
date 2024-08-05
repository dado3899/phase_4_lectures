# Setting up imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db,Computer

# Setting up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
db.init_app(app)

# Now lets run int the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5555
    # flask db init
    # flask db migrate -m 'Create tables productions'
    # flask db upgrade

# Lets create some Seed data!

# We can run the server with flask run and navigate to http://localhost:5555/`

# Routes
    # We can set up routes with @app.route('/')
@app.route('/')
def index():
    print("Hello")
    print("There")
    return f'<h1>FRONT END WITH PYTHON</h1>'

@app.route('/<input1>')
def show_word(input1):
    return f'<h1>{input1}</h1>'

@app.route('/dog')
def dog_route():
    print("Dog")
    return f'<img src="https://images.rawpixel.com/image_png_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvcHUyMzMxNzg4LWltYWdlLXJtNTAzLTAxXzEtbDBqOXFyYzMucG5n.png"/>'

@app.route("/post",methods=["POST"])
def pseudoPost():
    print("Definitely posting")
    return{}
    # Now lets set up a route that goes to the following image
    # If we have a dynamic route we can use 
        # @app.route('/<title>')
        #  def display(title):
        #     return f'<h1>{title}</h1>'
    # Lets use the class.query.filter() in order to filter like we were using
    # sqlAlchemy

@app.route("/computers")
def computer_route():
    all_comps = Computer.query.all()
    all_comps_dict = []
    for comp in all_comps:
        c = {
            "id": comp.id,
            "brand": comp.brand,
            "memory": comp.memory,
            "gpu": comp.gpu,
            "ram": comp.ram,
            "laptop": comp.laptop,
            "aesthetics": comp.aesthetics
        }
        all_comps_dict.append(c)
    return all_comps_dict

@app.route("/computers/<int:id>")
def one_computer(id):
    # Computer.query.filter_by(id = id).first()
    comp = Computer.query.filter(Computer.id == id).first()
    if comp:
        c = {
            "id": comp.id,
            "brand": comp.brand,
            "memory": comp.memory,
            "gpu": comp.gpu,
            "ram": comp.ram,
            "laptop": comp.laptop,
            "aesthetics": comp.aesthetics
        }
        return c
    else:
        return {
            "Error": "Id not found"
        }

# Request Hooks
    # @app.before_request: runs a function before each request.
    # @app.before_first_request: runs a function before the first request (but not subsequent requests).
    # @app.after_request: runs a function after each request.
    # @app.teardown_request: runs a function after each request, even if an error has occurred.

@app.before_request
def check():
    print("CHeck to see if user is logged in")
    user_logged_in = True
    if user_logged_in:
        print("Yay logged in")
    else:
        print("Nonono")
        return {
            "Error": "Tsk tsk tsk"
        }
    
@app.before_first_request
def sparkles():
    print("YAAAAAAYYY First one have sparkles")

# @app.after_request
# def countdown(res):
#     read_count = 1
#     if read_count > 0:    
#         #Minus read count      
#         return res
#     # else:
    #     return {
    #         "Error": "Stop freeloading buddy"
    #     }

@app.teardown_request
def teardown(err):
    print(err)



# Lets set up out main so we don't have to use flask run
if __name__ == '__main__':
    app.run(port=5555, debug=True)