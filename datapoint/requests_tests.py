import requests
from unittest.mock import Mock, patch

BASE_URI = 'api/datapoints'

data = [{
    'name': 'BRENT',
    'freq': 'm',
    'date': '2018-01-01',
    'value': 42.0
}]

payload = {'name': 'BRENT', 'freq': 'm'}
    

@patch('requests.get')
def test_request_response(mock_get):
    """Should complete successfully with OK status code"""
    mock_get.return_value = Mock(ok=True)

    response = requests.get(BASE_URI, params=payload)
    assert response.ok

@patch('requests.get')
def test_getting_BRENT(mock_get):
    """Should return a list with items that have the requested variable"""
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = data

    response = requests.get(BASE_URI, params=payload)
    assert response.json()[0]['name'] == 'BRENT'

@patch('requests.get')
def test_request_with_empty_name(mock_get):
    """Should return 400 error with empty name parameter"""
    payload = {'name': '', 'freq': 'm'}
    mock_get.return_value = Mock(status_code=400)

    response = requests.get(BASE_URI, params=payload)
    assert response.status_code == 400

@patch('requests.get')
def test_getting_data_not_found(mock_get):
    """Should return response with empty json"""
    payload = {'name': 'FOOBAR', 'freq': 'm'}
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = {}

    response = requests.get(BASE_URI, params=payload)
    assert response.json() == {}

# @patch('requests.get')
# def test_putting_data(mock_get):
# [{ "date": "1999-03-31", "freq": "q", "name": "INVESTMENT_bln_rub", "value": 12345.6 }]
