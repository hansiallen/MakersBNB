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

class SpaceRepository:
    def __init__(self):
        self.spaces = []

    def create_space(self, user_id, name, description, price_per_night, available_dates):
        if not name:
            raise ValueError("Name is required")
        
        space = Space(user_id, name, description, price_per_night, available_dates)
        self.spaces.append(space)
        return space

    def get_spaces(self):
        return self.spaces

    def delete_space(self, space_id):
        for space in self.spaces:
            if space.id == space_id:
                self.spaces.remove(space)
                return True  # Deletion successful
        return False  # Space not found