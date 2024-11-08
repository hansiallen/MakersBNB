from flask_login import UserMixin
from lib.utils.password_security import *
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
    
    def get_id(self):
        """Return the unique identifier for the user."""
        return str(self.email)  # Flask-Login needs a string return type

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):

        return f"User({self.id}, {self.email}, {self.password})"
    