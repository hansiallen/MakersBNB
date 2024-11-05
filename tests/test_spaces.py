import pytest
from spaces import Space, SpaceRepository

def test_create_space():
    # Initialise the repository
    repo = SpaceRepository()
    
    # Create a new unique space
    space = repo.create_space(
        user_id = 1,
        name = "Cute cottage",
        description = "A small, cute cottage in the woods",
        price_per_night = 50.0,
        available_dates = ["01-12-2024", "02-12-2024"]
    )
    
    # Assertions
    assert space.id == 1
    assert space.user_id == 1
    assert space.name == "Cute cottage"
    assert space.description == "A small, cute cottage in the woods"
    assert space.price_per_night == 50.0
    assert space.available_dates == ["01-12-2024", "02-12-2024"]

def test_create_multiple_spaces():
    # initialise the repository
    repo = SpaceRepository()

    # Create multiple spaces
    space1 = repo.create_space(
        user_id = 1,
        name = "Cute cottage",
        description = "A small, cute cottage in the woods",
        price_per_night = 50.0,
        available_dates = ["01-12-2024", "02-12-2024"]
    )
    space2 = repo.create_space(
        user_id = 2 ,
        name = "Beach House",
        description = "A beautiful beach house with ocean view",
        price_per_night = 200.0,
        available_dates =["08-12-2024", "09-12-2024"]
    )

    # Assertions for first space
    assert space1.id == 1
    assert space1.name == "Cute cottage"

    # Assertions for second space
    assert space2.id == 2
    assert space2.name == "Beach House"

def test_get_spaces():
    # initialise the repository
    repo = SpaceRepository()
    
    # Add a space
    repo.create_space(
        user_id = 1,
        name = "Cute cottage",
        description = "A small, cute cottage in the woods",
        price_per_night = 50.0,
        available_dates = ["01-12-2024", "02-12-2024"]
    )
    
    # Fetch spaces and validate
    spaces = repo.get_spaces()
    assert len(spaces) == 1
    assert spaces[0].name == "Cute cottage"

def test_create_space_invalid_data():
    # initialise the repository
    repo = SpaceRepository()

    # Try creating a space with an invalid name
    try:
        repo.create_space(
            user_id = 1,
            name = "",
            description = "A big mansion in the city",
            price_per_night = 500.0,
            available_dates=["01-10-2024", "02-10-2024"]
        )
    except ValueError as e:
        assert str(e) == "Name is required"
    else:
        assert False, "ValueError not raised"

def test_delete_space():
    # initialise the repository
    repo = SpaceRepository()

    # Add a space and delete it
    space = repo.create_space(
        user_id = 1,
        name = "Cute cottage",
        description = "A small, cute cottage in the woods",
        price_per_night = 50.0,
        available_dates = ["01-12-2024", "02-12-2024"]
    )
    space_id = space.id
    deletion_result = repo.delete_space(space_id)

    # Assertions
    assert deletion_result is True
    assert len(repo.get_spaces()) == 0

def test_delete_nonexistent_space():
    # initialise the repository
    repo = SpaceRepository()
    
    # Try deleting a non-existent space
    deletion_result = repo.delete_space(999)  # Using a non-existent ID
    assert deletion_result is False