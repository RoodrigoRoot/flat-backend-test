import pytest
from pulls.commits.serializers import AllCommitsSerializer, DetailsCommitSerializer
from Utils.repo import GitHubManage

def test_get_all_commits_serializer_succesfully(mocker, mock_all_commits):

    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_all_commits
    )
    response_commits = GitHubManage.get_all_commit()
    commits_serializer = AllCommitsSerializer(response_commits['data'], many=True)

    assert commits_serializer.data is not None
    assert commits_serializer.data[0]['sha'] is not None
    assert commits_serializer.data[0]['commit']['author']['name'] == 'Rodrigo Urcino'


def test_get_details_commit_serializer_succesfully(mocker, mock_details_commit):

    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_details_commit
    )
    commit_sha = '113446b77e491aadd665ba56b0df96a86630e78d'
    response_commits = GitHubManage.get_commit_by_sha(commit_sha)
    commits_serializer = DetailsCommitSerializer(response_commits['data'])

    assert commits_serializer.data is not None
    assert commits_serializer.data['sha'] is not None
    assert commits_serializer.data['commit']['author']['name'] == 'Rodrigo Urcino'
    assert commits_serializer.data['commit']['message'] is not None
