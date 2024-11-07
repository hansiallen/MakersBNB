# auth.py
from flask_login import LoginManager, UserMixin

# Initialize the login manager
login_manager = LoginManager()

# Simulate a "database" of users for simplicity
users = {"foo@bar.com": {"password": "secret"}}  # Example user

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return None
    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return None
    user = User()
    user.id = email
    return user
