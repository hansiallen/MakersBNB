from flask_login import LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from lib.user_repo import UserRepo
from lib .database_connection import DatabaseConnection

# Initialize the login manager
login_manager = LoginManager()
db_connection = DatabaseConnection()
db_connection.connect() 
user_repo = UserRepo(db_connection) 

class User(UserMixin):
    def __init__(self, email, password, user_id=None):
        self.id = user_id  # Will be assigned from the DB if not passed
        self.email = email
        self.password = password  # Store password (hashed)

    def verify_password(self, password):
        """Verify if the given password matches the stored hashed password."""
        return check_password_hash(self.password, password)  # Compare hashed passwords

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
