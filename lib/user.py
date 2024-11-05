class User:

    def __init__(self, id, email, name, password):
        if not email:
            raise ValueError("Email is required")
        self.id = id
        self.email = email
        self.name = name
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):

        return f"User({self.id}, {self.email}, {self.name}, {self.password})"
    