import json
import pytest
from django.shortcuts import reverse
import requests
import requests_mock

PULL_REQUEST_URL = 'http://localhost8000'+reverse('all_pulls')


@pytest.mark.django_db
def test_create_pull_request_status_open(mocker, mock_create_pull_status_open, mock_response_pull_status_open):
    with requests_mock.Mocker() as m:
        m.post(PULL_REQUEST_URL, json=mock_response_pull_status_open, status_code=201)
        response = requests.post(PULL_REQUEST_URL, json=mock_create_pull_status_open)
    response_json = response.json()

    assert response_json is not None
    assert response_json['success'] is True
    assert response_json['data']['id'] is not None
    assert response_json['data']['title'] == 'Pull request de prueba'
    assert response_json['data']['state'] == 'open'


@pytest.mark.django_db
def test_create_pull_request_status_merge(mocker, mock_create_pull_status_merge, mock_response_pull_status_merge):
    with requests_mock.Mocker() as m:
        m.post(PULL_REQUEST_URL, json=mock_response_pull_status_merge, status_code=201)
        response = requests.post(PULL_REQUEST_URL, json=mock_create_pull_status_merge)
    response_json = response.json()

    assert response_json is not None
    assert response_json['success'] is True
    assert response_json['data']['sha'] is not None
    assert response_json['data']['merged']  is True
    assert response_json['data']['message'] =='Pull Request successfully merged'
