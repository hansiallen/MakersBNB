from lib.spaces import Space

class SpacesRepo:
    def __init__(self):
        self.spaces = {}
        self.next_id = 1
    
    def create_space(self, id, user_id, name, description, price_per_night, available_dates):
        new_space = Space(id, user_id, name, description, price_per_night, available_dates)
        self.add_space(new_space)
        return new_space

    def add_space(self, space):
        space.id = self.next_id
        self.spaces[self.next_id] = space
        self.next_id += 1

    def remove_space(self, space_id):
        if space_id in self.spaces:
          del self.spaces[space_id]
          return True
        return False

    def get_space(self, space_id):
        return self.spaces.get(space_id)
    
    def list_spaces(self):
        return list(self.spaces.values())

    def find_available_spaces(self, start_date, end_date):
        available_spaces = []
        for space in self.spaces.values():
            if space.is_available(start_date, end_date):
                available_spaces.append(space)
        return available_spaces

    def book_space(self, space_id, start_date, end_date):
        space = self.get_space(space_id)
        if space and space.is_available(start_date, end_date):
            space.book(start_date, end_date)
            return True
        return False
    
