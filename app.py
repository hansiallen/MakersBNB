import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from lib.database_connection import get_flask_database_connection
from lib.spaces_repo import SpacesRepo
from lib.spaces import Space
from flask_login import login_required, current_user, logout_user, login_user
from lib.user_repo import UserRepo, User
from lib.auth import login_manager, LoginManager
from sqlalchemy.exc import IntegrityError

    

# Create a new Flask app
app = Flask(__name__)

# Secret key for session management (required by Flask-Login)
app.secret_key = 'your_secret_key'  # Change this to a secure key

# Initialize the login manager with the Flask app

login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to the login route when needed

@login_manager.user_loader
def load_user(user_id):
    user_repo = UserRepo(get_flask_database_connection(app))  # Assuming db_connection is initialized
    return user_repo.get_user_by_email(user_id)


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
    return render_template('/pages/list-spaces.html', spaces =spaces, logged_in= current_user.is_authenticated)


@app.route('/add-spaces',methods=['POST'])
def add_spaces_route():
    # take in all the information for the space and the users id
    # this page returns a link to redirect to the login screen if not logged in
    pass

@app.route('/space/<id>',methods=['GET'])
def get_space_info_route(id):
    spaces_repo = SpacesRepo(get_flask_database_connection(app))
    space = spaces_repo.get_space(id)

    # Maybe create a 404.html for this kind of thing
    if not space:
        return "Couldn't find the space you're looking for", 404
    
    return render_template('pages/space.html', space=space)


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        # Check if email or password is empty
        if not email or not password:
            flash('Email and password cannot be empty.', 'error')
            return redirect(url_for('sign_up'))  # Redirect back to the sign-up page
        
        # Check if the email is in a valid format (basic check)
        if '@' not in email or '.' not in email:
            flash('Invalid email format.', 'error')
            return redirect(url_for('sign_up'))  # Redirect back to the sign-up page
        
        try:
            # Creating a user in the repo with a hashed password
            user_repo = UserRepo(get_flask_database_connection(app))

            # Attempt to add the user
            user = user_repo.add_user(User(None, email, generate_password_hash(password)))
            
            # After adding, check if the user is added successfully
            user = user_repo.get_user_by_email(email)
            if user:
                print(f'User created: {user.email}')
                flash('User successfully created, you can log in now.', 'success')
                return redirect(url_for('login'))  # Redirect to the login page after successful sign-up
            else:
                flash('User not found after creation attempt.', 'error')
                return redirect(url_for('sign_up'))  # Redirect back if something went wrong

        except IntegrityError:
            # Catch database error related to duplicate email (unique constraint violation)
            flash('User already exists, please use a different email.', 'error')
            return redirect(url_for('sign_up'))  # Redirect back to the sign-up page if user exists
        
        except Exception as e:
            flash(f'User already exists, please use a different email.', 'error')  # Flash any exception message that occurs
            return redirect(url_for('sign_up'))  # Redirect back in case of error
    
    return render_template('/pages/sign-up.html')




@app.route('/about', methods=['GET'])
def render_about_page():
    return render_template('pages/about.html', is_about= True)

@app.route('/privacy', methods=['GET'])
def render_privacy_policy():
    return render_template('pages/privacy-policy.html')

@app.route('/tos', methods=['GET'])
def render_tos_page():
    return render_template('pages/tos.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.


# Routes

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            # Attempt to get email and password from the form
            email = request.form['email'].strip()
            password = request.form['password'].strip()
            
            # Check if either field is empty
            if not email or not password:
                flash('Email and password cannot be empty.', 'error')
                return redirect(url_for('login'))

            print(f'Attempting login with email: {email}')
            
            # Initialize UserRepo and fetch user by email
            user_repo = UserRepo(get_flask_database_connection(app))
            user = user_repo.get_user_by_email(email)
            
            if user:
                print(f'User found: {user.email}')
                
                # Check if the provided password matches the stored hash
                if check_password_hash(user.password, password):
                    print('Password is correct, logging in...')
                    login_user(user)
                    return redirect(url_for('protected'))  # Redirect on success
                else:
                    print('Incorrect password')
                    flash('Incorrect password', 'error')
            else:
                print('User not found')
                flash('User not found', 'error')

            # Redirect to login on failure
            return redirect(url_for('login'))

        except KeyError as e:
            # Handle missing form fields
            flash(f'Missing field: {e.args[0]}', 'error')
            return redirect(url_for('login'))
    
    # Render login form for GET request
    return render_template('pages/login.html')

# Protected route
@app.route('/protected', methods=['GET'])
@login_required  # Ensure the user is logged in to access this page
def protected():
    return f'Logged in as: {current_user.id}'

# Logout route
@app.route('/logout')
@login_required
def logout():
    print(f'Logged out user {current_user.id}')  # Optional debug info
    logout_user()  # Log the user out
    return redirect(url_for('get_spaces_route'))  # Redirect to spaces list after logout
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
