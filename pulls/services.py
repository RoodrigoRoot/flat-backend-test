import uuid
from typing import Dict

from Utils.repo import GitHubManage, CommitManage
from Utils.exceptions import FileWasNotCreatedException

def merge_pull_request(data: Dict) -> Dict:

    response_commit = create_commit_push()
    response: Dict = GitHubManage.create_pull_request(data, response_commit['branch_name'])
    if not response['success']:
        return response
    number :int = response['data']['number']
    response_merge: Dict = GitHubManage.merge_pull_request(number)
    return response_merge


def create_pull_request(data: Dict) -> Dict:
    response_commit = create_commit_push()
    response: Dict = GitHubManage.create_pull_request(data, response_commit['branch_name'])
    return response


def create_commit_push() -> Dict:
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
