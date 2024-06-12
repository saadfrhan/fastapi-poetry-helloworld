from fastapi.testclient import TestClient
from fastapi_poetry_helloworld.main import app

client = TestClient(app)


def test_root_path():
    # Send a GET request to the root path ('/')
    response = client.get("/")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected message
    assert response.json() == {"message": "Hey friend! Welcome to our wonderful world!"}


# Define a test function for the '/morning' path
def test_morning_path():

    # Send a GET request to the '/morning' path
    response = client.get("/morning")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected message
    assert response.json() == {"message": "Good morning sunshine! ☀️"}


# Define a test function for the '/night' path
def test_night_path():
    # Send a GET request to the '/night' path
    response = client.get("/night")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected message
    assert response.json() == {"message": "Good night, sleep tight! 🌙"}
