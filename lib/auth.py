from flask_login import LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# Initialize the login manager
login_manager = LoginManager()

# Simulate a "database" of users for simplicity
users = {
    "foo@bar.com": {"password": generate_password_hash("secret")}  # Store the password as a hash
}  # Example user

class User(UserMixin):
    def __init__(self, email=None):
        self.id = email  # Use email as the unique user ID

    def get_id(self):
        return self.id

    def verify_password(self, password):
        # Assuming you store a hashed password (as done with generate_password_hash)
        stored_password = users.get(self.id, {}).get('password')  # Fetch the stored hashed password
        if stored_password:
            return check_password_hash(stored_password, password)  # Verify the hash
        return False

# Setup the user_loader to load users by their email
@login_manager.user_loader
def user_loader(email):
    # Return the user if it exists, otherwise return None
    if email not in users:
        return None
    user = User(email)  # Create a user instance with the email as ID
    return user

# The request_loader can be used for request-based authentication
@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return None
    user = User(email)
    # Here you could add logic to automatically authenticate based on POST data
    return user
