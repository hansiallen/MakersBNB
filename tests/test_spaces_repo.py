from lib.spaces_repo import *

class Space:
    def __init__(self, space_id, name, description, price_per_night, available_dates):
        self.id = space_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.available_dates = available_dates

def test_add_space():
    """Test adding a new space"""
    spaces_repo = SpacesRepo()
    space = Space(1, "London flat", "spacious flat", 100, ["4/11/2024"])
    spaces_repo.add_space(space)
    assert len(spaces_repo.spaces) == 1
    assert spaces_repo.get_space(1) == space

def test_remove_space():
    """Test removing a new space"""
    spaces_repo = SpacesRepo()
    space = Space(1, "London flat", "spacious flat", 100, ["4/11/2024"])
    spaces_repo.add_space(space)
    spaces_repo.remove_space(1)
    assert len(spaces_repo.spaces) == 0
    assert spaces_repo.get_space(1) is None

def test_get_space():
    """Test getting space"""
    spaces_repo = SpacesRepo()
    space = Space(1, "London flat", "spacious flat", 100, ["4/11/2024"])
    spaces_repo.add_space(space)
    retrieved_space = spaces_repo.get_space(1)
    assert retrieved_space == space 
    non_existent_space = spaces_repo.get_space(2)
    assert non_existent_space is None
