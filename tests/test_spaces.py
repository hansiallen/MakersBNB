import pytest
from lib.spaces import Space

def test_is_equal():
    space = Space(1, 1, "london flat", "a small flat", 100.0)
    space2 = Space(1, 1, "london flat", "a small flat", 100.0)
    assert space == space2

def test_create_space():
    
    # Create a new unique space
    space =Space(
        id = 1,
        owner_id = 1,
        name = "Cute cottage",
        description = "A small, cute cottage in the woods",
        price_per_night = 50.0
    )
    
    # Assertions
    assert space.id == 1
    assert space.owner_id == 1
    assert space.name == "Cute cottage"
    assert space.description == "A small, cute cottage in the woods"
    assert space.price_per_night == 50.0

def test_create_multiple_spaces():

    # Create multiple spaces
    space1 = Space(
        id = 1,
        owner_id = 1,
        name = "Cute cottage",
        description = "A small, cute cottage in the woods",
        price_per_night = 50.0
    )
    space2 = Space(
        id = 2,
        owner_id = 2 ,
        name = "Beach House",
        description = "A beautiful beach house with ocean view",
        price_per_night = 200.0
    )

    # Assertions for first space
    assert space1.id == 1
    assert space1.name == "Cute cottage"

    # Assertions for second space
    assert space2.id == 2
    assert space2.name == "Beach House"
