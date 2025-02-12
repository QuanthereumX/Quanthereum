# auth.py - Authentication & Authorization for QuanthereumX
# Author: Przemek Buczek

import jwt
import bcrypt
import datetime
from config import SECRET_KEY

def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    """Checks if password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed.encode())

def generate_token(user_id):
    """Generates a JWT token for a user."""
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    """Verifies a JWT token and returns the payload if valid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Example usage
if __name__ == "__main__":
    test_password = "supersecret"
    hashed_pw = hash_password(test_password)
    print(f"🔒 Hashed Password: {hashed_pw}")

    is_valid = check_password(test_password, hashed_pw)
    print(f"✅ Password Valid: {is_valid}")

    token = generate_token(user_id=123)
    print(f"🎫 JWT Token: {token}")

    decoded = verify_token(token)
    print(f"🔑 Decoded Token: {decoded}")
