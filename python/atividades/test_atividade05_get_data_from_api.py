import pytest
from unittest.mock import patch
from atividade05_get_data_from_api import get_data_from_api
import requests

@patch('atividade05_get_data_from_api.requests.get')
def test_get_data_from_api_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {'key': 'value'}
    url = 'http://fakeapi.com/data'

    data = get_data_from_api(url)
    assert data == {'key': 'value'}
    mock_get.assert_called_once_with(url)

@patch('atividade05_get_data_from_api.requests.get')
def test_get_data_from_api_failure(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.side_effect = requests.exceptions.RequestException
    url = 'http://fakeapi.com/data'

    with pytest.raises(requests.exceptions.RequestException):
        get_data_from_api(url)
    mock_get.assert_called_once_with(url)

@patch('atividade05_get_data_from_api.requests.get')
def test_get_data_from_api_empty_response(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {}
    url = 'http://fakeapi.com/data'

    data = get_data_from_api(url)
    assert data == {}
    mock_get.assert_called_once_with(url)

@patch('atividade05_get_data_from_api.requests.get')
def test_get_data_from_api_different_data(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {'another_key': 'another_value'}
    url = 'http://fakeapi.com/data'

    data = get_data_from_api(url)
    assert data == {'another_key': 'another_value'}
    mock_get.assert_called_once_with(url)
    
if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade05_get_data_from_api.py","-vv"])
