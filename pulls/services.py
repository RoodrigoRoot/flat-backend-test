from typing import Dict

from Utils.repo import GitHubManage


def merge_pull_request(data: Dict) -> Dict:
    response: Dict = GitHubManage.create_pull_request(data)
    if not response['success']:
        return response
    number :int = response['data']['number']
    response_merge: Dict = GitHubManage.merge_pull_request(number)
    return response_merge


def create_pull_request(data: Dict) -> Dict:
    response: Dict = GitHubManage.create_pull_request(data)
    return response
