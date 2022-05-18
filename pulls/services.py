import uuid
from typing import Dict

from pulls.models import PullRequest
from Utils.repo import GitHubManage, CommitManage
from Utils.exceptions import FileWasNotCreatedException


def merge_pull_request(data: Dict) -> Dict:
    """
    With tis function we create a pull request with status merge, usign the
    class GitHubManage with his function create_pull_request and after
    merge_pull_request to manage all steps.
    """

    response_commit = create_commit_push()
    response: Dict = GitHubManage.create_pull_request(data, response_commit['branch_name'])
    if not response['success']:
        return response
    number :int = response['data']['number']
    response_merge: Dict = GitHubManage.merge_pull_request(number)
    save_pull_request(data)
    return response_merge


def create_pull_request(data: Dict) -> Dict:

    """
    With tis function we create a pull request with status open, usign the 
    class GitHubManage with his function create_pull_request to manage all steps.
    """

    response_commit = create_commit_push()
    response: Dict = GitHubManage.create_pull_request(data, response_commit['branch_name'])
    save_pull_request(data)
    return response


def create_commit_push() -> Dict:

    """
    This function is responsible for executing
    several methods to create a new branch,
    create new document, create commit and
    send push to Github
    """

    branch_name: str = 'branch_' + str(uuid.uuid4())[:4]
    try:
        CommitManage.create_branch(branch_name)
        response_document = CommitManage.create_document()
        if not response_document['success']:
            raise FileWasNotCreatedException('El archivo no pudo ser creado')
        file_name = response_document['file_name']
        CommitManage.create_commit(file_name)
        GitHubManage.send_push(branch_name)
        return {'success': True, 'branch_name': branch_name}
    except Exception as e:
        print(e)
        return {'success': False, 'errors': str(e)}


def save_pull_request(data: Dict) -> PullRequest:

    """
    With this function we create a row of
    Pull Request on DB.
    """

    try:
        pull_request = PullRequest(**data)
        pull_request.save()
        return PullRequest
    except Exception as e:
        print(e)
        return False
