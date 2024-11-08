import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from lib.database_connection import get_flask_database_connection
from lib.spaces_repo import SpacesRepo
from lib.spaces import Space
from flask_login import login_required, current_user, logout_user, login_user
from lib.user_repo import UserRepo, User
from lib.auth import login_manager, LoginManager

    

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


@app.route('/add-spaces', methods=['GET', 'POST'])
#@login_required  # Ensure only logged-in users can add spaces
def add_spaces_route():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        description = request.form.get('description')
        price_per_night = request.form.get('price-per-night')
        available_from = request.form.get('available-from')
        available_to = request.form.get('available-to')

        # Basic validation
        if not name or not price_per_night or not available_from or not available_to:
            flash("All fields are required.", "error")
            return redirect(url_for('add_spaces_route'))

        # Add space to the database
        try:
            repo = SpacesRepo(get_flask_database_connection(app))
            space = Space(
                id=None, 
                owner_id=current_user.id, # Logged in user as the owner
                name=name,
                description=description,
                price_per_night=float(price_per_night)
            )
            repo.add_space(space)
            flash("Space listed successfully!", "success")
            return redirect(url_for('get_spaces_route'))
        except Exception as e:
            print(e)  # Debugging
            flash("Error listing space.", "error")
            return redirect(url_for('add_spaces_route'))

    return render_template('pages/add-spaces.html')


@app.route('/space/<id>',methods=['GET'])
def get_space_info_route(id):
    spaces_repo = SpacesRepo(get_flask_database_connection(app))
    space = spaces_repo.get_space(id)

    # Maybe create a 404.html for this kind of thing
    if not space:
        return "Couldn't find the space you're looking for", 404
    
    return render_template('pages/space.html', space=space)


@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    # takes username, email and password from a form
    # should give a return message as a either
    #  sucseffuly created in or incorrect email or password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f'Attempting login with email: {email}')
        
        user_repo = UserRepo(get_flask_database_connection(app))
        user = user_repo.add_user(User(None,email,generate_password_hash(password)))
        user = user_repo.get_user_by_email(email)
        if user:
            print(f'User found: {user.email}')
            if check_password_hash(user.password, password):
                print('Password is correct, logging in...')
                login_user(user)
                return redirect(url_for('protected'))  # Redirect to the protected page after successful login
            else:
                print(user.password)
                print(password)
                print('Incorrect password')
                flash('Incorrect password', 'error')
        else:
            print('User not found')
            flash('User not found', 'error')
        
        # If login fails, redirect to the login page with a flash message
        return redirect(url_for('login'))
    
    # should return a full login page
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
        email = request.form['email']
        password = request.form['password']
        print(f'Attempting login with email: {email}')
        
        user_repo = UserRepo(get_flask_database_connection(app))
        user = user_repo.get_user_by_email(email)
        if user:
            print(f'User found: {user.email}')
            if check_password_hash(user.password, password):
                print('Password is correct, logging in...')
                login_user(user)
                return redirect(url_for('protected'))  # Redirect to the protected page after successful login
            else:
                print(user.password)
                print(password)
                print('Incorrect password')
                flash('Incorrect password', 'error')
        else:
            print('User not found')
            flash('User not found', 'error')
        
        # If login fails, redirect to the login page with a flash message
        return redirect(url_for('login'))
    
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
