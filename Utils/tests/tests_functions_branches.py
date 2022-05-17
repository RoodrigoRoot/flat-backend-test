import pytest
from Utils import repo
from Utils.repo import GitHubManage


def test_get_all_branches(mocker, mock_all_branches):

    mocker.patch(
      'Utils.repo.request_GET',
      return_value=mock_all_branches
    )
    response_branches = GitHubManage.get_all_branches()
    assert response_branches is not None
    assert type(response_branches) == dict
    assert type(response_branches['data']) == list
    assert response_branches['data'][0]['name'] is not None
