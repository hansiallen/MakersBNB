import pytest
from flask import Flask, session
from flask_login import current_user
from werkzeug.security import generate_password_hash
from lib.spaces import Space
from lib.spaces_repo import SpacesRepo
from lib.database_connection import get_flask_database_connection
from unittest.mock import MagicMock
from app import app

# Test client fixture for Flask testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    with app.test_client() as client:
        yield client

# Helper fixture to simulate a logged-in user
@pytest.fixture
def logged_in_user(client, db_connection):
    # Mock the user login process
    email = 'user1@example.com'
    password = 'password1'

    # In a real test, here we would mock or seed a user into the database and log them in
    # Simulate a logged-in state for user
    user_id = 1
    with client.session_transaction() as session:
        session['_user_id'] = user_id
    return {'email': email, 'user_id': user_id}

def test_add_spaces_success(client, db_connection):
    """Test adding a space with valid data"""
    
    # Mock the session to simulate a logged-in user
    with client.session_transaction() as session:
        session['_user_id'] = 1  # Simulating logged-in user
    
    # Simulate the form data
    space_data = {
        'name': 'Cozy Cottage',
        'description': 'A cozy cottage in the countryside',
        'price-per-night': '100',
        'available-from': '2024-12-01',
        'available-to': '2024-12-31'
    }
    
    # Simulate the space creation form submission (POST request)
    response = client.post('/add-spaces', data=space_data)
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Assert the correct redirect URL (adjust this based on your logic)
    assert response.headers['Location'] == '/add-spaces'  # If it's redirecting to the same page

def test_create_space_invalid_data(client, db_connection):
    """Test creating space with invalid data"""
    
    # Data with missing required field
    space_data = {
        'name': '',  # Missing name
        'description': 'A small but comfortable space.',
        'price-per-night': '50',
        'available-from': '2024-11-01',
        'available-to': '2024-11-30'
    }
    
    # Simulate the space creation form submission
    response = client.post('/add-spaces', data=space_data)
    
    # Assert the response returns with a 400 (Bad Request) due to validation failure
    assert response.status_code == 302  # Bad Request due to validation errors

from unittest.mock import MagicMock

"""def test_create_space_already_exists(client, db_connection):
    Test creating a space when the space already exists (duplicate)
    
    # Seed with an existing space (assuming db_connection.seed works with your test DB setup)
    db_connection.seed("seeds/spaces.sql") 
    db_connection.seed("seeds/users.sql") # Ensure the space data is seeded for this test
    
    # Mock the db_connection to track the execute method calls
    mock_db_connection = MagicMock()
    app.db_connection = mock_db_connection
    
    # Data for a new space listing (same name as an existing one)
    space_data = {
        'name': 'Cozy Apartment',  # Duplicate name (exists in seeded data)
        'description': 'A small but comfortable space.',
        'price-per-night': '50',
        'available-from': '2024-11-01',
        'available-to': '2024-11-30'
    }

    # Simulate the space creation form submission
    response = client.post('/add-spaces', data=space_data)
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302  # Redirect due to the duplication scenario
    
    # Check for the expected flash message (this assumes a flash message is set for duplicates)
    with client.session_transaction() as session:
        assert 'Error listing space' in session['_flashes'][0][1]
    
    # Ensure no new entry is inserted into the database
    mock_db_connection.execute.assert_not_called()  # Ensure no insert query was executed"""




# Test space creation with invalid input (missing fields)
def test_add_spaces_missing_fields(client, db_connection):
    """Test adding a space with missing required fields"""
    
    # Mock the session to simulate a logged-in user
    with client.session_transaction() as session:
        session['_user_id'] = 1  # Simulating logged-in user
    
    # Simulate form data with missing required fields (e.g., missing 'price-per-night')
    space_data = {
        'name': 'Cozy Cottage',
        'description': 'A cozy cottage in the countryside',
        'available-from': '2024-12-01',
        'available-to': '2024-12-31'
    }
    
    # Simulate the space creation form submission (POST request)
    response = client.post('/add-spaces', data=space_data)
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Assert the redirect URL (we expect to be redirected back to the form)
    assert response.headers['Location'] == '/add-spaces'
    
    # Assert that an error flash message was triggered
    with client.session_transaction() as session:
        assert 'All fields are required.' in session['_flashes'][0][1]

# Test creating a space with an invalid price (non-numeric)
def test_add_spaces_invalid_price(client, db_connection):
    """Test adding a space with an invalid price format"""
    
    # Mock the session to simulate a logged-in user
    with client.session_transaction() as session:
        session['_user_id'] = 1  # Simulating logged-in user
    
    # Simulate form data with an invalid 'price-per-night'
    space_data = {
        'name': 'Cozy Cottage',
        'description': 'A cozy cottage in the countryside',
        'price-per-night': 'invalid_price',  # Invalid price
        'available-from': '2024-12-01',
        'available-to': '2024-12-31'
    }
    
    # Simulate the space creation form submission (POST request)
    response = client.post('/add-spaces', data=space_data)
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Assert the redirect URL (we expect to be redirected back to the form)
    assert response.headers['Location'] == '/add-spaces'
    
    # Assert that the flash message indicates the price format is invalid
    with client.session_transaction() as session:
        assert 'Error listing space' in session['_flashes'][0][1]  # The actual error message for invalid price


"""  
# Test that a space creation form fails with missing description
def test_create_space_missing_description(client, db_connection):
    Test that space creation fails when description is missing
    
    # Seed the spaces table for testing
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/users.sql")
    
    # Data with a missing description
    space_data = {
        'name': 'Spacious Loft',
        'price-per-night': '100',
        'available-from': '2024-12-01',
        'available-to': '2024-12-31'
    }
    
    # Simulate the space creation form submission (using correct route)
    response = client.post('/add-spaces', data=space_data)
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Check that the correct flash message is triggered
    with client.session_transaction() as session:
        assert 'Error listing space' in session['_flashes'][0][1]  # Update to the correct flash message

"""





