import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from lib.database_connection import get_flask_database_connection
from lib.spaces_repo import SpacesRepo
from flask_login import login_required, current_user
from lib.spaces import Space

# Create a new Flask app
app = Flask(__name__)

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
                id=None,  # ID will be auto-generated
                owner_id=current_user.id,  # Logged-in user as the owner
                name=name,
                description=description,
                price_per_night=float(price_per_night)
            )
            repo.add_space(space)
            flash("Space listed successfully!", "success")
            return redirect(url_for('get_spaces_route'))
        except Exception as e:
            print(e)  # Log the error for debugging
            flash("Error listing space.", "error")
            return redirect(url_for('add_spaces_route'))

    # If GET request, render the add-space form
    return render_template('pages/add-spaces.html')

@app.route('/space/<id>',methods=['GET'])
def get_space_info_route(id):
    connnection = get_flask_database_connection()
    spaces_repo = SpacesRepo(connnection)
    space = spaces_repo.get_space(id)

    # Maybe create a 404.html for this kind of thing
    if not space:
        return "Couldn't find the space you're looking for", 404
    
    return render_template('pages/space.html', space=space)

@app.route('/login', methods=['GET'])
def get_login_route():
    # should return a full login page
    return render_template('login.html')

@app.route('/login', methods=['POST'])
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
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
