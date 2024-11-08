import pytest
from flask import Flask
from flask_login import current_user
from app import app  # Import your Flask app
from lib.auth import User
from werkzeug.security import generate_password_hash
from mock import Mock
from lib.user_repo import UserRepo
from unittest.mock import MagicMock

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    with app.test_client() as client:
        yield client

def test_login_valid_user(client, db_connection):
    """Test logging in with valid credentials using mock data (no real database needed)"""
    
    # Mock user data (hashed password)
    mock_user_data = {
        'email': 'user1@example.com',
        'password': generate_password_hash('password1')  # This is the correct hashed password
    }
    
    # Create a mock UserRepo to simulate database interaction
    mock_user_repo = MagicMock()
    
    # Simulate the behavior of getting the user by email
    mock_user_repo.get_user_by_email.return_value = mock_user_data
    
    # Patch the app's user repo to use the mock
    app.user_repo = mock_user_repo

    # Simulate logging in with valid credentials (mocking the POST request)
    response = client.post('/login', data={'email': 'user1@example.com', 'password': 'password1'})
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Assert the redirect URL is the protected route (i.e., after successful login)
    assert response.headers['Location'] == '/protected'
    
    # Check that the mock user is logged in after the login attempt
    with client.session_transaction() as session:
        # Ensure the session has '_user_id' key (simulating user login)
        assert '_user_id' in session  # Mocked login will store the user_id in session
        assert session['_user_id'] == mock_user_data['email']  # Mocked session data (user's email)


def test_login_invalid_user(client, db_connection):
    """Test logging in with invalid credentials"""
    # Seed the database with some user data if needed
    db_connection.seed("seeds/users.sql")
    
    # Attempt login with invalid credentials (user does not exist)
    response = client.post('/login', data={'email': 'invalid@bar.tld', 'password': 'wrong'})
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Ensure that the redirect location is still the login page (or wherever the app redirects)
    assert response.headers['Location'] == '/login'

def test_protected_route_requires_login(client):
    """Test that accessing the protected route requires login"""
    # Attempt to access a protected route without login
    response = client.get('/protected')
    
    # Assert that the response is a redirect (302)
    assert response.status_code == 302
    
    # Assert that the location is the login page
    assert '/login' in response.headers['Location']

def test_logout(client):
    """Test logging out after a successful login"""
    # Perform the logout action
    response = client.get('/logout')  # Simulate the logout request

    # Assert logout success (should redirect to a page like home or login page)
    assert response.status_code == 302  # Should redirect after logout

def test_login_blank_fields(client):
    """Test login with blank email or password to trigger flash messages."""

    # Attempt to login with blank email and password
    response = client.post('/login', data={'email': '', 'password': ''})
    
    # Ensure it redirects back to the login page
    assert response.status_code == 302
    assert response.headers['Location'] == '/login'
    
    # Follow the redirect and check for flash message
    follow_response = client.get('/login', follow_redirects=True)
    assert b'Email and password cannot be empty.' in follow_response.data
    
def test_login_invalid_password(client):
    """Test logging in with an incorrect password"""
    
    # Mock user data for correct credentials
    mock_user_data = {
        'email': 'user1@example.com',
        'password': 'password1'  # Correct password for this test
    }
    
    # Simulate the behavior of getting the user by email
    mock_user_repo = MagicMock()
    mock_user_repo.get_user_by_email.return_value = mock_user_data
    
    # Patch the app's user repo to use the mock
    app.user_repo = mock_user_repo

    # Simulate logging in with the correct email but incorrect password
    response = client.post('/login', data={'email': 'user1@example.com', 'password': 'wrongpassword'})
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Check that the user is redirected back to the login page
    assert response.headers['Location'] == '/login'
    
    # Check that the flash message indicates incorrect password
    with client.session_transaction() as session:
        assert 'Incorrect password' in session['_flashes'][0][1]

def test_login_user_not_found(client):
    """Test logging in with an email that does not exist"""
    
    # Simulate the behavior of the user repo returning None (user not found)
    mock_user_repo = MagicMock()
    mock_user_repo.get_user_by_email.return_value = None  # No user found
    
    # Patch the app's user repo to use the mock
    app.user_repo = mock_user_repo

    # Simulate logging in with a non-existing email
    response = client.post('/login', data={'email': 'nonexistent@example.com', 'password': 'any'})
    
    # Assert the response is a redirect (status code 302)
    assert response.status_code == 302
    
    # Check that the user is redirected back to the login page
    assert response.headers['Location'] == '/login'
    
    # Check that the flash message indicates user not found
    with client.session_transaction() as session:
        assert 'User not found' in session['_flashes'][0][1]
