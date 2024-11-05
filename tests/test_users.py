from lib.user import *

def test_user_constucts():
    user = User(1,'user1@example.com', 'User One', 'password1')
    assert user.id == 1
    assert user.email == 'user1@example.com'
    assert user.name == 'User One'
    assert user.password == 'password1'

def test_users_format_nicely():
    user = User(1, 'user1@example.com', 'User One', 'password1')
    assert str(user) == "User(1, user1@example.com, User One, password1)"

def test_users_are_equal():
    user1 = User(1,'user1@example.com', 'User One', 'password1')
    user2 = User(1,'user1@example.com', 'User One', 'password1')
    assert user1 == user2

def test_users_are_not_equal_different_ids():
    user1 = User(1, 'user1@example.com', 'User One', 'password1')
    user2 = User(2, 'user1@example.com', 'User One', 'password1')
    assert user1 != user2