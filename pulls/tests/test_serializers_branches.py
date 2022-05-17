import pytest
from pulls.branches.serializers import AllBranchesSerializer, DetailBranchSerializer
from Utils.repo import GitHubManage

def test_get_all_branches_serializer_succesfully(mocker, mock_all_branches):

    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_all_branches
    )
    response_branches = GitHubManage.get_all_branches()
    branches_serializer = AllBranchesSerializer(response_branches['data'], many=True)

    assert branches_serializer.data is not None
    assert branches_serializer.data[0]['name'] is not None
    assert type(branches_serializer.data[0]['protected']) == bool


def test_get_details_branch_serializer_succesfully(mocker, mock_detail_branch):

    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_detail_branch
    )
    branch_name = 'main'
    response_branch = GitHubManage.get_branch_detail(branch_name)
    branch_serializer = DetailBranchSerializer(response_branch['data'])


    assert branch_serializer.data is not None
    assert branch_serializer.data['name'] == 'main'
    assert branch_serializer.data['commit'] is not None
