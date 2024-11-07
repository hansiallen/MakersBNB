from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, email, password):
        if not email:
            raise ValueError("Email is required")
        self.id = id
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.password})"

    def get_id(self):
        return str(self.id)
    
    def verify_password(self, password):

        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

        
    