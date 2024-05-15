import source.service as service
import pytest
import unittest.mock as mock
import requests_mock

@mock.patch("source.service.get_user_from_database")  # mock
def test_get_user(mock_database):
    result = mock_database.return_value = "admin"
    user = service.get_user_from_database(1)
    assert user == result

# othre way
""" @mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }
    mock_get.return_value = mock_response
    data = service.get_users(1)
    assert data == mock_response.json.return_value """


# Comparation the data from the API with the data value
def test_get_users_success():
    # Simular la respuesta de la API
    user_data = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }
    with requests_mock.Mocker() as mock:
        mock.get("https://jsonplaceholder.typicode.com/users/1", json=user_data)

        # Llamar a la función a probar
        result = service.get_users(1)

        # Verificar que se devuelve el resultado esperado
        assert result == user_data

@mock.patch('source.service.requests.get')
def test_get_users_failure(mock_get):
    # Simular una respuesta fallida de la API
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Llamar a la función a probar
    result = service.get_users(1)

    # Verificar que se devuelve None
    assert result is None