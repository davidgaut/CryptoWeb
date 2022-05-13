import pytest # Pytest is a good tool to test your application
import json

from app import app # Import your API

@pytest.fixture # Fixtures are reusable mocked object in Python
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client # Return an in memory API for launching the test

def test_hello_world(client): # Instanciate the API in memory
    res = client.get('/hello_world') # Send a GET request on the route /hello_world
    assert b'Hello World!' == res.data # Verify that the result is correct
