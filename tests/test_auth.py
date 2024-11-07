import pytest
from flask import Flask
from flask_login import current_user
from app import app  # Import your Flask app
from lib.auth import login_manager, User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    with app.test_client() as client:
        yield client

def test_login_valid_user(client, user_repo):
    # Hash the password before storing
    hashed_password = generate_password_hash('secret')
    
    # Create a valid user instance with hashed password
    user = User(email='foo@bar.com', password=hashed_password)
    
    # Add the user to the database
    user_repo.add_user(user)
    
    # Attempt login with valid credentials
    response = client.post('/login', data={'email': 'foo@bar.com', 'password': 'secret'})
    
    # Assert the status code is 302 (redirect)
    assert response.status_code == 302
    
    # Assert the redirect URL is /protected
    assert response.headers['Location'] == '/protected'

def test_login_invalid_user(client, user_repo):
    # Attempt login with invalid credentials
    response = client.post('/login', data={'email': 'invalid@bar.tld', 'password': 'wrong'})
    
    # Assert the error message for invalid credentials
    assert b'Invalid credentials' in response.data
    
    # Assert that the user is not authenticated
    assert not current_user.is_authenticated

def test_protected_route_requires_login(client):
    # Attempt to access a protected route without login
    response = client.get('/protected')
    
    # Assert that the response is a redirect (302)
    assert response.status_code == 302
    
    # Assert that the location is the login page
    assert '/login' in response.headers['Location']

def test_logout(client):
    # Log in first
    response = client.post('/login', data={'email': 'foo@bar.com', 'password': 'secret'})
    assert response.status_code == 302  # Ensure login redirects

    # Now access the protected route
    protected_response = client.get('/protected', follow_redirects=True)
    assert protected_response.status_code == 200  # Should have access

    # Log out
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200  # Ensure logout redirects to home

    # Attempt to access protected route again after logout
    protected_response = client.get('/protected')
    assert protected_response.status_code == 302  # Should redirect to login