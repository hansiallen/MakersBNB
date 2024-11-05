import pytest
from lib.user_repo import UserRepo

@pytest.fixture
def user_repo():
    return UserRepo()

def test_create_user(user_repo):
    user = user_repo.add_user(1, "Adam", "adam@gmail.com", "password123")
    assert user['id'] == 1  # Check that the user ID is 1
    assert user['name'] == "Adam"
    assert user['email'] == "adam@gmail.com"
    assert user['password'] == "password123"

def test_get_user(user_repo):
    user_repo.add_user(1, "Adam", "adam@gmail.com", "password123")
    user = user_repo.get_user(1)
    assert user['name'] == "Adam"

def test_user_exists(user_repo):
    user_repo.add_user(1, "Adam", "adam@gmail.com", "password123")
    assert user_repo.user_exists("adam@gmail.com") is True
    assert user_repo.user_exists("nonexistent@gmail.com") is False

def test_get_all_users(user_repo):
    # Add users with unique IDs
    user_repo.add_user(1, "Adam", "adam@gmail.com", "password123")
    user_repo.add_user(2, "Tobi", "tobi@gmail.com", "password456")
    
    # Retrieve all users and verify
    all_users = user_repo.get_all_users()

    # Assertions
    assert len(all_users) == 2  # Ensure two users were created

    # Verify user details
    user_dict = {user['id']: user for user in all_users}
    
    assert user_dict[1] == {'id': 1, 'name': "Adam", 'email': "adam@gmail.com", 'password': "password123"}
    assert user_dict[2] == {'id': 2, 'name': "Tobi", 'email': "tobi@gmail.com", 'password': "password456"}

def test_remove_existing_user(user_repo):
    # Create a user
    user = user_repo.add_user(1, "Adam", "adam@gmail.com", "password123")
    
    # Verify user creation
    assert user_repo.get_user(user['id']) == user  # Check if the user exists before removal.

    # Now, remove the user
    result = user_repo.remove_user(user['id'])  # Remove the user using the created user's ID.

    # Assertions
    assert result is True  # The result should indicate success
    assert user_repo.get_user(user['id']) is None  # User should no longer exist


def test_remove_nonexistent_user(user_repo):
    # Attempt to remove a user that does not exist
    result = user_repo.remove_user(999)  # ID 999 does not exist

    # Assertions
    assert result is False  # The result should indicate failure
