from flask_login import LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from lib.user_repo import UserRepo
from lib .database_connection import DatabaseConnection
from lib.utils.password_security import *

# Initialize the login manager
login_manager = LoginManager()
db_connection = DatabaseConnection()
db_connection.connect() 
user_repo = UserRepo(db_connection) 

class User(UserMixin):
    def __init__(self, user_id, email, password, active=True):
        self.id = user_id
        self.email = email
        self.password = password
        self.active = active
    
    
    def is_authenticated(self):
        return True if self.id else False
    
    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def verify_password(self, password):
        hashed_data = hash_password(self.password)
        """Verify if the given password matches the stored hashed password."""
        return verify_password(password, hashed_data['salt'], hashed_data['hashed_password'])  # Compare hashed passwords

    def get_id(self):
        """Return the unique identifier for the user."""
        return str(self.id)  # Flask-Login needs a string return type
    
    def get_user_by_email(self, email):
    # Assume this returns a dictionary-like object from your DB
    # e.g., {"user_id": 1, "email": "foo@bar.com", "password": "hashed_password"}
        pass

# Setup the user_loader to load users by their email
@login_manager.user_loader
def user_loader(email):
    # Fetch user from the database by email using UserRepo
    user_data = user_repo.get_user_by_email(email)
    if user_data:
        return User(user_data['user_id'], user_data['email'], user_data['password'])
    return None

# The request_loader can be used for request-based authentication
@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    # Fetch user from the database by email using UserRepo
    user_data = user_repo.get_user_by_email(email)
    if user_data:
        return User(user_data['user_id'], user_data['email'], user_data['password'])
    return None
