import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def get_index():
    return render_template('/pages/list-spaces.html')


@app.route('/login', methods=['GET'])
def get_login():
    # should return a full login page
    return render_template('/pages/login.html')

@app.route('/add-spaces',methods=['POST'])
def get_spaces():
    # take in all the information for the space and the users id
    # this page returns a link to redirect to the login screen if not logged in
    pass

@app.route('/space',methods=['GET'])
def add_spaces():
    # have an argument with the space id to show the correct space
    return render_template('/pages/space.html')


@app.route('/login', methods=['POST'])
def try_login():
    # takes email and password from a form
    # should give a return message as a either
    #  'sucseffuly logged in' or 'incorrect email or password'
    pass


# @app.route('/sign_up', methods=['GET'])
# def get_sign_up():
#     # should return a full login page
#     return render_template('/sign-up.html')


@app.route('/sign-up', methods=['GET'])
def get_sign_up():
    return render_template('/pages/sign-up.html')

@app.route('/sign-up', methods=['POST'])
def try_sign_up():
    # takes username, email and password from a form
    # should give a return message as a either
    #  sucseffuly created in or incorrect email or password
    pass

@app.route('/login', methods=['GET'])
def get_login():
    # should return a full login page
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def try_login():
    # takes email and password from a form
    # should give a return message as a either
    #  'sucseffuly logged in' or 'incorrect email or password'
    pass


@app.route('/sign_up', methods=['GET'])
def get_login():
    # should return a full login page
    return render_template('login.html')

@app.route('/sign_up', methods=['POST'])
def try_sign_up():
    # takes name, email and password from a form
    # should give a return message as a either
    #  'sucseffuly logged in' or 'incorrect email or password'
    pass

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
