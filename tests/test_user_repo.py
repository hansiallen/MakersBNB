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
        id = None,
        email='user1@example.com',
        password='password1',
    )
    
    # Add the user to the database
    user_id = user_repo.add_user(user)
    
    # Assertions
    assert user_id is not None  # Check that the user ID is returned

def test_remove_user():
    """Test removing a user"""
    # Create a mock database connection
    db_connection = Mock()

    # Create a mock result object with a rowcount attribute
    mock_result = Mock()
    mock_result.rowcount = 1  # Simulate that 1 row was affected (deleted)

    # Mock the database execute method for deletion and checking existence
    db_connection.execute.side_effect = [
        [{'user_id': 1, 'email': 'user1@example.com', 'password': 'password1'}],  # For initial get_user
        mock_result  # For delete operation, return mock result
    ]

    # Initialize UserRepo with the mock connection
    user_repo = UserRepo(db_connection)

    # Add a user to ensure they exist before removal
    user_repo.add_user(User(id=1, email="user1@example.com", password="password1"))

    # Call remove_user to delete the user with ID 1
    result = user_repo.remove_user(1)

    # Assertions to verify that the user was successfully removed
    assert result is True  # Should return True because the mock result simulates success

def test_get_user():
    """Test getting a user"""
    # Create a mock database connection
    db_connection = Mock()

    # Set up the mock to return a single user record when queried
    db_connection.execute.return_value = [
        {'user_id': 1, 'email': 'user1@example.com', 'password': 'password1'}
    ]

    # Initialize UserRepo with the mock connection
    user_repo = UserRepo(db_connection)

    # Call get_user to fetch user with ID 1
    user = user_repo.get_user(1)

    # Assertions to verify that the returned user matches the expected data
    assert user.id == 1
    assert user.email == 'user1@example.com'
    assert user.password == 'password1'

def test_get_multiple_users():
    """Test getting multiple users"""
    # Create a mock database connection
    db_connection = Mock()

    # Set up the mock to return a sample data set when queried (no 'name' field)
    db_connection.execute.return_value = [
        {'user_id': 1, 'email': 'user1@example.com', 'password': 'password1'},
        {'user_id': 2, 'email': 'user2@example.com', 'password': 'password2'},
    ]
    
    # Initialize UserRepo with the mock connection
    user_repo = UserRepo(db_connection)

    # Retrieve all users
    users = user_repo.list_users()

    # Assertions
    assert len(users) == 2
    assert users[0].email == 'user1@example.com'
    assert users[0].password == 'password1'
    assert users[1].email == 'user2@example.com'
    assert users[1].password == 'password2'
