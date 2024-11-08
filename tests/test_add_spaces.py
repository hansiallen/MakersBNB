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

def test_create_space_invalid_data(client, logged_in_user, db_connection):
    """Test creating space with invalid data"""

    # Data with missing required field
    space_data = {
        'name': '',  # Missing name
        'description': 'A small but comfortable space.',
        'price-per-night': '50',
        'location': 'New York',
        'capacity': '2',
        'available-from': '2024-11-01',
        'available-to': '2024-11-30'
    }

    # Simulate the space creation form submission
    response = client.post('/create-space-listing', data=space_data)

    # Assert the response returns with a 400 (Bad Request) due to validation failure
    assert response.status_code == 400  # Bad Request due to validation errors
    
    # Check for the expected error message (e.g., "Name is required")
    follow_response = client.get('/create-space-listing', follow_redirects=True)
    assert b'Name is required' in follow_response.data

def test_create_space_already_exists(client, logged_in_user, db_connection):
    """Test creating a space when the space already exists (duplicate)"""
    
    # Seed with an existing space
    db_connection.seed("seeds/spaces.sql")  # Assuming your spaces table has data already
    
    # Data for a new space listing (same name as an existing one)
    space_data = {
        'name': 'Cozy Apartment',  # Duplicate name
        'description': 'A small but comfortable space.',
        'price-per-night': '50',
        'location': 'New York',
        'capacity': '2',
        'available-from': '2024-11-01',
        'available-to': '2024-11-30'
    }

    # Simulate the space creation form submission
    response = client.post('/create-space-listing', data=space_data)

    # Assert the response returns with a 409 (Conflict) due to duplication
    assert response.status_code == 409  # Conflict error for trying to add a space that already exists
    
    # Check for the expected flash message
    with client.session_transaction() as session:
        assert 'Space already exists' in session['_flashes'][0][1]
    
    # Ensure no new entry is inserted into the database
    db_connection.execute.assert_not_called()  # No insert should happen


# Test space creation with invalid input (missing fields)
def test_create_space_missing_field(client, logged_in_user, db_connection):
    """Test that a space creation fails if required fields are missing"""

    # Seed the spaces table for testing
    db_connection.seed("seeds/spaces.sql")
    
    # Data with a missing field (missing name)
    space_data = {
        'description': 'A small but comfortable space.',
        'price-per-night': '50',
        'location': 'New York',
        'available-from': '2024-11-01',
        'available-to': '2024-11-30'
    }

    # Simulate the space creation form submission
    response = client.post('/create-space-listing', data=space_data)

    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    assert response.headers['Location'] == '/create-space-listing'  # Stay on the form page on error

    # Check for flash message indicating missing fields
    with client.session_transaction() as session:
        assert 'All fields are required.' in session['_flashes'][0][1]

# Test creating a space with an invalid price (non-numeric)
def test_create_space_invalid_price(client, logged_in_user, db_connection):
    """Test that creating a space with an invalid price fails"""

    # Seed the spaces table for testing
    db_connection.seed("seeds/spaces.sql")
    
    # Data with an invalid price (non-numeric)
    space_data = {
        'name': 'Luxury Condo',
        'description': 'A luxurious space.',
        'price-per-night': 'invalid-price',
        'location': 'Los Angeles',
        'available-from': '2024-12-01',
        'available-to': '2024-12-31'
    }

    # Simulate the space creation form submission
    response = client.post('/create-space-listing', data=space_data)

    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    assert response.headers['Location'] == '/create-space-listing'  # Stay on the form page on error

    # Check for flash message indicating the invalid price
    with client.session_transaction() as session:
        assert 'Invalid price per night.' in session['_flashes'][0][1]

# Test that a space creation form fails with missing description
def test_create_space_missing_description(client, logged_in_user, db_connection):
    """Test that space creation fails when description is missing"""

    # Seed the spaces table for testing
    db_connection.seed("seeds/spaces.sql")
    
    # Data with a missing description
    space_data = {
        'name': 'Spacious Loft',
        'price-per-night': '100',
        'location': 'San Francisco',
        'available-from': '2024-12-01',
        'available-to': '2024-12-31'
    }

    # Simulate the space creation form submission
    response = client.post('/create-space-listing', data=space_data)

    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    assert response.headers['Location'] == '/create-space-listing'  # Stay on the form page on error

    # Check for flash message indicating missing description
    with client.session_transaction() as session:
        assert 'All fields are required.' in session['_flashes'][0][1]

# Test successful space listing and redirection
def test_space_list_page(client, db_connection):
    """Test the spaces listing page displays added spaces"""

    # Seed the spaces table with data
    db_connection.seed("seeds/spaces.sql")

    # Get the spaces listing page
    response = client.get('/spaces')

    # Assert that the response contains the spaces we seeded
    assert response.status_code == 200
    assert b'Cozy Apartment' in response.data  # Ensure the space name appears on the list
    assert b'Luxury Condo' in response.data  # Ensure another space appears

