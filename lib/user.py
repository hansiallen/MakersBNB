class User:

    def __init__(self, id, email, password):
        if not email:
            raise ValueError("Email is required")
        self.id = id
        self.email = email
        self.password = password
        self.active = True
    
    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active
    
    def get_id(self):
        """Return the unique identifier for the user."""
        return str(self.email)  # Flask-Login needs a string return type

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):

        return f"User({self.id}, {self.email}, {self.password})"
    