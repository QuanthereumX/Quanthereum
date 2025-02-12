# api.py - REST API for QuanthereumX
# Author: Przemek Buczek

from fastapi import FastAPI, HTTPException, Depends
from auth import generate_token, verify_token
from services import fetch_data
from pydantic import BaseModel

app = FastAPI()

# Dummy authentication
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    """Simulates user login and returns a JWT token."""
    # In a real app, you'd check the password in the database!
    if request.username == "admin" and request.password == "password":
        token = generate_token(user_id=1)
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/")
def home():
    """Main endpoint."""
    return {"message": "Welcome to QuanthereumX API"}

@app.get("/users")
def get_users():
    """Example database query to fetch all users."""
    query = "SELECT * FROM users;"
    data = fetch_data(query)
    if data:
        return {"users": data}
    raise HTTPException(status_code=404, detail="No users found")

@app.get("/protected")
def protected_route(token: str = Depends(verify_token)):
    """Example of a protected route that requires authentication."""
    if token:
        return {"message": "You have access!", "user": token["user_id"]}
    raise HTTPException(status_code=401, detail="Invalid or expired token")

# Run API with: uvicorn src.api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
