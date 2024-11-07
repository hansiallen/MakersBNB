import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from lib.database_connection import get_flask_database_connection
from lib.spaces_repo import SpacesRepo
from lib.spaces import Space
from lib.auth import login_manager, User, LoginManager
from flask_login import login_required, current_user, logout_user, login_user
# Create a new Flask app
app = Flask(__name__)

app.secret_key = "mysecretkey"
users = {'email@test.com': generate_password_hash('password123')}

login_manager.init_app(app)

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
    return render_template('pages/list-spaces.html', spaces=spaces)


@app.route('/add-spaces',methods=['POST'])
def add_spaces_route():
    # take in all the information for the space and the users id
    # this page returns a link to redirect to the login screen if not logged in
    pass

@app.route('/space/<id>',methods=['GET'])
def get_space_info_route(id):
    # have an argument with the space id to show the correct space
    return render_template('pages/space.html')

@app.route('/login', methods=['GET', 'POST'])
def get_login_route():
    if current_user.is_authenticated:
        print("User already logged in")
        return redirect('/')
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(f"Login attempt with email: {email}")
        
        if email in users and check_password_hash(users[email], password):
            user = User(email)
            login_user(user)

            return redirect('/')
        
        else:
            print("Invalid login attempt")
            error = 'Invalid email/password combination'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Log the user out
    logout_user()
    # Redirect to the list of spaces page (or homepage)
    return redirect(url_for('get_spaces_route'))  # Redirect to the route that renders the list of spaces

    

@app.route('/home')
def home():
    if current_user.is_authenticated:
    
        return render_template('pages/list-spaces.html', email=current_user.email)
    else:
        return redirect('/login')



@app.route('/sign-up', methods=['GET'])
def get_sign_up_route():
    # should return a full login page
    return render_template('pages/sign-up.html')



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

def load_user(user_id):
    return User(user_id)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

# Routes

@app.route('/protected')
@login_required
def protected():
    return f'Logged in as: {current_user.id}'

