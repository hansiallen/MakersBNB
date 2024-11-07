import pytest
from flask import Flask
from flask_login import current_user
from app import app  # Import your Flask app
from lib.auth import login_manager, User  # Assuming these are defined in your auth.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    with app.test_client() as client:
        yield client

def test_login_valid_user(client):
    # Mock a valid user login
    response = client.post('/login', data={'email': 'foo@bar.com', 'password': 'secret'})
    
    # Assert the status code is 302 (redirect)
    assert response.status_code == 302
    
    # Assert the redirect URL is /protected
    assert response.headers['Location'] == '/protected'

def test_login_invalid_user(client):
    # Attempt login with invalid credentials
    response = client.post('/login', data={'email': 'invalid@bar.tld', 'password': 'wrong'})
    assert b'Invalid credentials' in response.data
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
    assert response.status_code == 302  # Ensure login worked

    # Now, check if the user is logged in by accessing a protected route
    protected_response = client.get('/protected')
    assert protected_response.status_code == 200  # Should be accessible if logged in

    # Log out
    response = client.get('/logout')

    # Assert the status code is 302 (redirect)
    assert response.status_code == 302
    
    # Assert that the redirect location is the get spaces page (or homepage)
    assert response.headers['Location'] == '/'  # This matches the redirect to the get spaces page

    client.cookie_jar.clear()

    assert not current_user.is_authenticated  

    # Try accessing a protected route again after logout
    protected_response = client.get('/protected')

    # Ensure the user is redirected to the login page (since they're logged out)
    assert protected_response.status_code == 302  # Should redirect to /login
    assert '/login' in protected_response.headers['Location']