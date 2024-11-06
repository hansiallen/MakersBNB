import hashlib
import os
import hmac

def hash_password(password: str) -> dict:
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return {'salt': salt, 'hashed_password': hashed_password}

def verify_password(password: str, salt: bytes, hashed_password: bytes) -> bool:
    test_hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hmac.compare_digest(test_hashed_password, hashed_password)

# ADAM AND TOBI: Read below for info on how to implement
"""
if __name__ == "__main__":
    # hash password:
    
    password = "my_secure_password"
    hashed_data = hash_password(password)
    print("Salt:", hashed_data['salt'])
    print("Hashed Password:", hashed_data['hashed_password'])
    

    # verify 2 passwords against stored hashed passwords, one is correct and one fails:

    input_password = "my_secure_password"  # Try the correct password
    is_verified = verify_password(input_password, hashed_data['salt'], hashed_data['hashed_password'])
    print("Password verification with correct password:", "Success" if is_verified else "Failure")
    
    input_password = "wrong_password"  # Try an incorrect password
    is_verified = verify_password(input_password, hashed_data['salt'], hashed_data['hashed_password'])
    print("Password verification with incorrect password:", "Success" if is_verified else "Failure")
"""

