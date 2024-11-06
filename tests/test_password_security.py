import pytest
from lib.utils.password_security import hash_password, verify_password

def test_hash_password_returns_salt_and_hash():
    password = "test_password"
    hashed_data = hash_password(password)
    
    assert 'salt' in hashed_data
    assert 'hashed_password' in hashed_data
    
    assert isinstance(hashed_data['salt'], bytes)
    assert isinstance(hashed_data['hashed_password'], bytes)

def test_verify_password_with_correct_password():
    password = "test_password"
    hashed_data = hash_password(password)
    
    assert verify_password(password, hashed_data['salt'], hashed_data['hashed_password']) is True

def test_verify_password_with_incorrect_password():
    password = "test_password"
    hashed_data = hash_password(password)
    
    assert verify_password("wrong_password", hashed_data['salt'], hashed_data['hashed_password']) is False

def test_hash_uniqueness():
    password = "test_password"
    hashed_data_1 = hash_password(password)
    hashed_data_2 = hash_password(password)
    
    assert hashed_data_1['hashed_password'] != hashed_data_2['hashed_password']
    assert hashed_data_1['salt'] != hashed_data_2['salt']

