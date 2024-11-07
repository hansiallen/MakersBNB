from lib.user_repo import UserRepo
from unittest.mock import Mock
from lib.user import User

def test_add_user(db_connection):
    """Test adding a new user"""
    # Seed the database with the users.sql data
    db_connection.seed("seeds/users.sql")
    
    # Initialize UserRepo with the database connection
    user_repo = UserRepo(db_connection)
    
    # Create a new user without setting the id (it will be auto-generated)
    user = User(
        user_id = None,
        email='user4@example.com',
        password='password1',
    )
    
    # Add the user to the database
    user_id = user_repo.add_user(user)
    
    # Assertions
    assert user_id is not None  # Check that the user ID is returned

def test_remove_user(db_connection):
    """Test removing a user"""
    # Seed the database with the users.sql data
    db_connection.seed("seeds/users.sql")
    
    # Initialize UserRepo with the actual database connection
    user_repo = UserRepo(db_connection)
    
    # Create a new user (without setting the id, it will be auto-generated)
    user = User(
        user_id = 1,  # ID will be auto-generated
        email="user4@example.com",
        password="password1"
    )
    
    # Add the user to the database and get the auto-generated user_id
    user_id = user_repo.add_user(user)
    
    # Assertions: Ensure the user ID is returned and is not None
    assert user_id is not None, "User ID should not be None"
    
    # Check that the user exists in the database by querying with the generated ID
    result = db_connection.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    assert len(result) == 1, f"User with ID {user_id} should exist in the database"
    
    # Now, call remove_user to delete the user with the generated user_id
    result = user_repo.remove_user(user_id)
    
    # Final check: Ensure the user no longer exists in the database
    result = db_connection.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    assert len(result) == 0, f"User with ID {user_id} should have been deleted"

def test_get_user(db_connection):
    """Test getting a user"""
    db_connection.seed("seeds/users.sql")

    # Initialize UserRepo with the connection
    user_repo = UserRepo(db_connection)

    # Call get_user to fetch user with ID 1
    user = user_repo.get_user(1)

    # Assertions to verify that the returned user matches the expected data
    assert user.id == 1
    assert user.email == 'user1@example.com'
    assert user.password == 'scrypt:32768:8:1$S3VeFkMUqtf7mwHw$68cf3b8e7f2897b3e3e6ecc4ad225f105ed4ca19cba629bd5cb5d9b59e8dec1986cc8f3fa3bdc566946b94fbc83d92afc2ca05d00a90238fa03271423d8199ef'

def test_get_multiple_users(db_connection):
    """Test getting multiple users"""
    db_connection.seed("seeds/users.sql")

    # Initialize UserRepo with the connection
    user_repo = UserRepo(db_connection)

    # Retrieve all users
    users = user_repo.list_users()

    # Assertions
    assert len(users) == 3
    assert users[0].email == 'user1@example.com'
    assert users[1].email == 'user2@example.com'
    assert users[2].email == 'user3@example.com'
