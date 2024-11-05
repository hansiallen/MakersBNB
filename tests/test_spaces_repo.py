from lib.spaces_repo import SpacesRepo
from mock import Mock

def test_add_space():
    """Test adding a new space"""
    spaces_repo = SpacesRepo()
    space = Mock()
    space.id = 1
    spaces_repo.add_space(space)
    assert len(spaces_repo.spaces) == 1
    assert spaces_repo.get_space(1) == space

def test_remove_space():
    """Test removing a new space"""
    spaces_repo = SpacesRepo()
    space = Mock()
    space.id = 1
    spaces_repo.add_space(space)
    spaces_repo.remove_space(1)
    assert len(spaces_repo.spaces) == 0

def test_get_space():
    """Test getting space"""
    spaces_repo = SpacesRepo()
    space = Mock()
    space.id = 1
    spaces_repo.add_space(space)
    retrieved_space = spaces_repo.get_space(1)
    assert retrieved_space == space

def test_get_multiple_spaces():
    """Test getting space"""
    spaces_repo = SpacesRepo()
    space1 = Mock()
    space1.id = 1
    spaces_repo.add_space(space1)
    space2 = Mock()
    space2.id = 2
    spaces_repo.add_space(space2)
    space3 = Mock()
    space3.id = 3
    spaces_repo.add_space(space3)
    retrieved_space = spaces_repo.get_space(2)
    assert retrieved_space == space2
    spaces_repo.remove_space(2)
    assert spaces_repo.get_space(2) == None