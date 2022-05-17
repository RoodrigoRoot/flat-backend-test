from pulls.serializers import CreatePullRequestSerializer, PullRequestSerializer
from Utils.repo import GitHubManage

def test_to_create_pull_request_status_open(mocker, mock_create_pull_status_open, mock_response_pull_status_open):
    mocker.patch(
        'Utils.repo.request_POST',
        return_value=mock_response_pull_status_open
    )

    serializer_pull_request = CreatePullRequestSerializer(data=mock_create_pull_status_open)
    serializer_pull_request.is_valid(raise_exception=True)

    response_pull_request = GitHubManage.create_pull_request(serializer_pull_request.data)

    assert serializer_pull_request.is_valid() is True
    assert serializer_pull_request.data is not None
    assert response_pull_request is not None
    assert response_pull_request['success'] is True
    assert response_pull_request['data']['id'] is not None
    assert response_pull_request['data']['title'] == 'Pull request de prueba'
    assert response_pull_request['data']['state'] == 'open'


def test_to_create_pull_request_status_merge(mocker, mock_create_pull_status_merge, mock_response_pull_status_merge):
    mocker.patch(
        'Utils.repo.request_POST',
        return_value=mock_response_pull_status_merge
    )

    serializer_pull_request = CreatePullRequestSerializer(data=mock_create_pull_status_merge)
    serializer_pull_request.is_valid(raise_exception=True)

    response_pull_request = GitHubManage.create_pull_request(serializer_pull_request.data)

    assert serializer_pull_request.is_valid() is True
    assert serializer_pull_request.data is not None
    assert response_pull_request is not None
    assert response_pull_request['success'] is True
    assert response_pull_request['data']['sha'] is not None
    assert response_pull_request['data']['merged']  is True
    assert response_pull_request['data']['message'] =='Pull Request successfully merged'
