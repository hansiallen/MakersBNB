class SpacesRepo:
    def __init__(self):
        self.spaces = {}

    def add_space(self, space):    
        self.spaces[space.id] = space

    def get_space(self, space_id):
        return self.spaces.get(space_id)

    def remove_space(self, space_id):
        if space_id in self.spaces:
            del self.spaces[space_id]
    
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