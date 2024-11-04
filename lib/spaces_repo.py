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