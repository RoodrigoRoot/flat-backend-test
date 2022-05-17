import pytest
from pulls.serializers import PullRequestSerializer, CreatePullRequestSerializer
from Utils.repo import GitHubManage


def test_serializer_all_pull_request_succesfully(mocker, mock_all_pulls):
    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_all_pulls
    )
    pull_request_response = GitHubManage.get_all_pull_request()
    pull_serializer = PullRequestSerializer(pull_request_response['data'], many=True)

    assert pull_serializer.data is not None
    assert type(pull_serializer.data[0]['number']) == int


def test_serializer_details_pull_request_succesfully(mocker, mock_details_pull):
    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_details_pull
    )
    pull_request_response = GitHubManage.get_all_pull_request()
    pull_serializer = PullRequestSerializer(pull_request_response['data'])

    assert pull_serializer.data is not None
    assert type(pull_serializer.data['number']) == int


def test_serializer_to_create_pull_request_status_open(mock_create_pull_status_open):

    serializer_pull_request = CreatePullRequestSerializer(data=mock_create_pull_status_open)
    serializer_pull_request.is_valid(raise_exception=True)

    assert serializer_pull_request.is_valid() is True
    assert serializer_pull_request.data is not None


def test_serializer_to_create_pull_request_status_merge(mock_create_pull_status_merge):

    serializer_pull_request = CreatePullRequestSerializer(data=mock_create_pull_status_merge)
    serializer_pull_request.is_valid(raise_exception=True)

    assert serializer_pull_request.is_valid() is True
    assert serializer_pull_request.data is not None