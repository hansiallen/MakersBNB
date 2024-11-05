import pytest
from lib.spaces import Space
from lib.spaces_repo import SpacesRepo

@pytest.fixture
def setup_spaces_repo():
    # Set up a new SpacesRepo instance before each test
    repo = SpacesRepo()
    yield repo
    # Clean up if needed after each test

def test_create_and_retrieve_space(setup_spaces_repo):
    repo = setup_spaces_repo
    space = Space(1, 1, "London flat", "A small flat in the city", 50.0, ["01-12-2024", "02-12-2024"])
    
    # Add the space to the repository
    repo.add_space(space)
    
    # Retrieve the space by ID
    retrieved_space = repo.get_space(1)
    
    # Assertions to ensure the space was added and retrieved correctly
    assert retrieved_space is not None
    assert retrieved_space.name == "London flat"
    assert retrieved_space.description == "A small flat in the city"

def test_remove_space(setup_spaces_repo):
    repo = setup_spaces_repo
    space = Space(1, 1, "London flat", "A small flat in the city", 50.0, ["01-12-2024", "02-12-2024"])
    repo.add_space(space)

    # Now remove the space
    repo.remove_space(1)
    
    # Attempt to retrieve the space
    retrieved_space = repo.get_space(1)
    
    # The space should no longer exist
    assert retrieved_space is None

def test_delete_nonexistent_space(setup_spaces_repo):
    repo = setup_spaces_repo
    # Attempt to remove a space that does not exist
    result = repo.remove_space(999)  # Assuming 999 is a non-existent ID
    assert result is False  # Adjust based on how your remove_space handles this

def test_create_multiple_spaces(setup_spaces_repo):
    repo = setup_spaces_repo
    
    # Create multiple spaces
    space1 = repo.create_space(
        id = 1,
        user_id=1,
        name="Beach House",
        description="A beautiful house by the beach",
        price_per_night=120.0,
        available_dates=["01-10-2024", "02-10-2024"]
    )
    
    space2 = repo.create_space(
        id = 2,
        user_id=2,
        name="Country House",
        description="A peaceful house in the countryside",
        price_per_night=80.0,
        available_dates=["01-12-2024", "02-12-2024"]
    )
    
    # Retrieve all spaces
    all_spaces = repo.list_spaces()
    
    # Assertions
    assert len(all_spaces) == 2  # Ensure two spaces were created
    assert space1.id in [s.id for s in all_spaces]
    assert space2.id in [s.id for s in all_spaces]

def test_space_validation():
    # Create a valid space
    space = Space(1, 1, "Luxury Villa", "A luxurious villa with a pool", 200, ["01-01-2025"])
    
    # Assertions to ensure the space is created properly
    assert space.name == "Luxury Villa"
    assert space.price_per_night == 200
    assert space.available_dates == ["01-01-2025"]
    
    # Testing invalid data (assuming you have validation in place)
    with pytest.raises(ValueError):  # Adjust based on your validation method
        Space(2, 2, "", "Invalid space", -100, [])