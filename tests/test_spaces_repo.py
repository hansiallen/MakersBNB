from lib.spaces_repo import *
from lib.spaces import Space

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

def test_get_space():
    """Test getting space"""
    spaces_repo = SpacesRepo()
    space = Space(1, "London flat", "spacious flat", 100, ["4/11/2024"])
    spaces_repo.add_space(space)
    retrieved_space = spaces_repo.get_space(1)
    assert retrieved_space == space
