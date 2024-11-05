class Space:
    _id_counter = 1  # Class-level counter for unique IDs

    def __init__(self, id, user_id, name, description, price_per_night):
        if not name:
            raise ValueError("Name is required")
        self.user_id = user_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night

        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.user_id}, {self.name}, {self.description}, {self.price_per_night})"
