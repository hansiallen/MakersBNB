class Space:
    _id_counter = 1  # Class-level counter for unique IDs

    def __init__(self, user_id, name, description, price_per_night, available_dates):
        if not name:
            raise ValueError("Name is required")
        self.user_id = user_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.available_dates = available_dates
        self.id = Space._id_counter
        Space._id_counter += 1