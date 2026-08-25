from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_successful_registration():

    response = client.post(
        "/register",
        json={
            "name": "Rani",
            "email": "rani@gmail.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "Employee registered successfully"


def test_empty_name():

    response = client.post(
        "/register",
        json={
            "name": "",
            "email": "rani@gmail.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Employee name is required"


def test_empty_email():

    response = client.post(
        "/register",
        json={
            "name": "Rani",
            "email": ""
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Email is required"


def test_invalid_email():

    response = client.post(
        "/register",
        json={
            "name": "Rani",
            "email": "ranigmail.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Invalid email format"


def test_duplicate_email():

    client.post(
        "/register",
        json={
            "name": "John",
            "email": "john@gmail.com"
        }
    )

    response = client.post(
        "/register",
        json={
            "name": "John Again",
            "email": "john@gmail.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Email already exists"


def test_get_employees():

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert "employees" in data

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "API Running"