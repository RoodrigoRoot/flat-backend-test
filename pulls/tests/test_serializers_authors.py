from pulls.authors.serializers import AllAuthorsSerializer
from Utils.repo import GitHubManage

def test_get_all_authors_serializer_succesfully(mocker, mock_authors):

    mocker.patch(
        'Utils.repo.request_GET',
        return_value=mock_authors
    )
    response_authors = GitHubManage.get_all_authors()
    authors_serializer = AllAuthorsSerializer(response_authors['data'], many=True)

    assert authors_serializer.data is not None
