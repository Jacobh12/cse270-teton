import requests

# ------------------------------
# Test 1: Valid login => 200
# ------------------------------
def test_login_admin_valid_returns_200(mocker):
    # Mock the requests.get call
    mock_get = mocker.patch("requests.get")

    # Configure the mock to return a fake response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mock_get.return_value = mock_response

    # Call the function (this will use mocked requests.get)
    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "qwerty"}
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 200
    assert response.text == ""


# ------------------------------
# Test 2: Invalid login => 401
# ------------------------------
def test_login_admin_invalid_returns_401(mocker):
    # Mock the requests.get call
    mock_get = mocker.patch("requests.get")

    # Configure the mock to return a fake response object
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mock_get.return_value = mock_response

    # Call the function (mocked)
    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "admin"}
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 401
    assert response.text == ""
