"""
Justin Wu
May 5, 2026
Lab 19: Unit test for veryfying authentication in a Flask-SQlite app
"""

import os 
import sqlite3
import pytest
from app import app
# ----------------------
# TEST DATABASE SETUP
# ----------------------
TEST_DB = 'test_flask_auth.db'

def init_rest_db():
    # Simulate a database connection
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # Create a template table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Create a mock database to run the app.py file\
@pytest.fixture
def client(monkeypatch):
    # Override database to use test database
    def test_get_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn
    
    # Match the mock database
    from app import get_db
    monkeypatch.setattr('app.get_db', test_get_db)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'

    # Call function to run the mock database
    init_rest_db()

    # create an instance of the Flask test client
    with app.test_client() as client:
        # yield means returns the client and after the all tests are finished the code resumes
        yield client

    # cleanup test database after tests
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

# ----------------------
# TEST HOME REDIRECT
# ----------------------
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302 
#   assert '/login' in response.location  # response.location means properly redirect to the URL location

# ----------------------
# TEST LOGIN SUCCESS
# ----------------------
def test_login_success(client):
    # First create a user to test the login later
    client.post('/signup', data={
        "username": "loginuser",
        "email": "loginuser@example.com",
        "password": "123456"
    })

    # Test the login with the user infor above
    response = client.post('/login', data={
        "email": "loginuser@example.com",
        "password": "123456"
    }, follow_redirects=True)  

    # Assert testing
    assert response.status_code == 200
    # Convert the <h1> Welcome </h1> in dashboard.html into bytes object
    assert b"Welcome" in response.data  

# ----------------------
# TEST LOGIN FAILURE
# ----------------------
def test_login_failure(client):
    response = client.post('/login', data={
        "email": "login@example.com",
        "password": "wrong123"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data 

# ----------------------
# TEST SIGNUP
# ----------------------
def test_signup(client):
    response = client.post('/signup', data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "123456"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Account created successfully!" in response.data 