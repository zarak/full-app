import requests

from unittest.mock import Mock, patch
from urllib.parse import urljoin


BASE_URI = ''
BRENT_URI = urljoin(BASE_URI, 'BRENT/m')

data = [{
    'name': 'BRENT',
    'freq': 'm',
    'date': '2018-01-01',
    'value': 42.0
}]
    

@patch('requests.get')
def test_request_response(mock_get):
    """Should complete successfully with OK status code"""
    mock_get.return_value = Mock(ok=True)

    response = requests.get(BRENT_URI)
    assert response.ok

@patch('requests.get')
def test_getting_BRENT(mock_get):
    """Should return a list with items that have the requested variable"""
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = data

    response = requests.get(BRENT_URI)
    assert response.json()[0]['name'] == 'BRENT'

# @patch('requests.get')
# def test_putting_data(mock_get):


