import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from lib.database_connection import get_flask_database_connection
from lib.spaces_repo import SpacesRepo
from lib.spaces import Space
from lib.auth import login_manager, User, LoginManager
from flask_login import login_required, current_user, logout_user, login_user

from lib.user_repo import UserRepo
from lib.database_connection import DatabaseConnection

db_connection = DatabaseConnection()
db_connection.connect() 
user_repo = UserRepo(db_connection)  

# Create a new Flask app
app = Flask(__name__)

# Secret key for session management (required by Flask-Login)
app.secret_key = 'your_secret_key'  # Change this to a secure key

# Initialize the login manager with the Flask app

login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to the login route when needed


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index

@app.route('/index', methods=['GET'])
def get_index_route():
    return render_template('index.html')

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def get_spaces_route():
    repo = SpacesRepo(get_flask_database_connection(app))
    spaces =repo.list_spaces()
    return render_template('/pages/list-spaces.html', spaces =spaces)


@app.route('/add-spaces',methods=['POST'])
def add_spaces_route():
    # take in all the information for the space and the users id
    # this page returns a link to redirect to the login screen if not logged in
    pass

@app.route('/space/<id>',methods=['GET'])
def get_space_info_route(id):
    # have an argument with the space id to show the correct space
    return render_template('/pages/space.html')

app.route('/login', methods=['GET'])
def get_login_route():
    # should return a full login page
    return render_template('/pages/login.html')

app.route('/login', methods=['POST'])
def try_login_route():
    # takes email and password from a form
    # should give a return message as a either
    #  'sucseffuly logged in' or 'incorrect email or password'
    pass


@app.route('/sign-up', methods=['GET'])
def get_sign_up_route():
    # should return a full login page
    return render_template('/pages/sign-up.html')



@app.route('/sign-up', methods=['POST'])
def try_sign_up_route():
    # takes username, email and password from a form
    # should give a return message as a either
    #  sucseffuly created in or incorrect email or password
    pass

@app.route('/about', methods=['GET'])
def render_about_page():
    return render_template('pages/about.html')

@app.route('/privacy', methods=['GET'])
def render_privacy_policy():
    return render_template('pages/privacy-policy.html')

@app.route('/tos', methods=['GET'])
def render_tos_page():
    return render_template('pages/tos.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

# Routes

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    user = user_repo.get_user_by_email(email)  # Fetch user from DB
    if user and check_password_hash(user.password, password):
        login_user(user)  # Log the user in using Flask-Login
        return redirect('/protected')
    
    return "Invalid credentials", 401  # Or appropriate error handling

@app.route('/protected', methods=['GET'])  # Ensure GET is allowed
@login_required
def protected():
    return f'Logged in as: {current_user.id}'

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    return redirect(url_for('get_spaces_route'))  # Redirect to another page (e.g., homepage or list of spaces)

if __name__ == '__main__':
    app.run(debug=True)