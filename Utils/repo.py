import json
import subprocess
import uuid
from typing import Dict
from abc import ABC, abstractclassmethod

from django.conf import settings
import requests


HEADERS_GITHUB = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {settings.TOKEN_GIT}',
    'Accept': 'application/vnd.github.v3+json'
    }

BODY_CREATE_PULL = {
    #'owner':'roodrigorot',
    'title':'',
    'body':'',
    'head':'test/pull',
    'base': 'test/merge'
}

def request_POST(url, data: Dict) ->Dict:
    try:
        response = requests.post(url, headers=HEADERS_GITHUB, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()
        return {'success': True, 'data': response_json}
    except Exception as e:
        error_response = {'success': False, 'message': str(e)}
        errors = response.json()
        reason = errors['errors'][0]['message']
        error_response['reason'] = reason
        return error_response


def request_PUT(url: str) -> Dict:
    try:
        response = requests.put(url, headers=HEADERS_GITHUB)
        response.raise_for_status()
        response_json = response.json()
        return {'success': True, 'data': response_json}
    except Exception as e:
        print(e)
        return {'success': False}


def request_GET(url) -> Dict:
    try:
        response = requests.get(url, headers=HEADERS_GITHUB)
        response.raise_for_status()
        response_json = response.json()
        return {'success': True, 'data': response_json}
    except Exception as e:
        return {'success': False, 'message': str(e)}


class HubManage(ABC):

    @abstractclassmethod
    def get_all_commit(cls):
        ...

    @abstractclassmethod
    def get_commit_by_sha(cls, sha):
        ...

    @abstractclassmethod
    def get_all_branches(cls):
        ...

    @abstractclassmethod
    def get_branch_detail(cls, branch):
        ...

    @abstractclassmethod
    def get_all_pull_request(cls):
        ...

    @abstractclassmethod
    def create_pull_request(cls, data: Dict):
        ...


class GitHubManage(HubManage):

    @classmethod
    def get_all_commit(cls) -> Dict:
        print("<------ Get All Commits ------>")
        url = f"{settings.GIT_URL}/commits"
        response_commits = request_GET(url)
        print(response_commits)
        if not response_commits:
            return None
        return response_commits

    @classmethod
    def get_commit_by_sha(cls, sha: str) -> Dict:
        print("<------ Get Commit by Sha ------>")
        url = f"{settings.GIT_URL}/commits/{sha}"
        response_commit = request_GET(url)
        print(response_commit)
        return response_commit

    @classmethod
    def get_all_branches(cls) -> Dict:
        print("<------ Get All Branch ------>")
        url = f"{settings.GIT_URL}/branches"
        response_branches = request_GET(url)
        print(response_branches)
        if not response_branches:
            return None
        return response_branches

    @classmethod
    def get_branch_detail(cls, branch: str) -> Dict:
        print("<------ Get Branch Details ------>")
        url = f"{settings.GIT_URL}/branches/{branch}"
        response_branch= request_GET(url)
        print(response_branch)
        if not response_branch:
            return None
        return response_branch

    @classmethod
    def get_all_authors(cls) -> Dict:
        print("<------ GET All Authors ------>")
        url = f"{settings.GIT_URL}/collaborators"
        response_authors = request_GET(url)
        return response_authors


    @classmethod
    def get_all_pull_request(cls) -> Dict:
        print("<------ Get Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls"
        response_pull= request_GET(url)
        print(response_pull)
        if not response_pull:
            return None
        return response_pull

    @classmethod
    def get_details_pull_request(cls, number: int) -> Dict:
        print("<------ Get Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls/{number}"
        response_pull= request_GET(url)
        print(response_pull)
        if not response_pull:
            return None
        return response_pull


    @classmethod
    def create_pull_request(cls, data: Dict) -> Dict:
        print("<------ Create Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls"
        BODY_CREATE_PULL['title'] = data['title']
        BODY_CREATE_PULL['body'] = data['description']
        response_pull = request_POST(url, BODY_CREATE_PULL)
        return response_pull


    @classmethod
    def merge_pull_request(cls, number: int):
        print("<------ Merge Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls/{number}/merge"
        response_pull = request_PUT(url)
        return response_pull


    @classmethod
    def send_push():
        ...


class CommitManage:

    @classmethod
    def create_branch(cls, name_branch: str) -> bool:
        try:
            subprocess.run(f'git checkout -b {name_branch}')
            return True
        except Exception as e:
            return False

    @classmethod
    def create_document(cls) -> bool:
        try:
            subprocess.run(f'touch doc_{str(uuid.uuid4())[:5]+"txt"}')
            return True
        except Exception as e:
            return False


    @classmethod
    def create_commit(cls):
        try:
            subprocess.run(f'git add . ; git commit -m "Test: Commit new file"')
            return True
        except Exception as e:
            return False



