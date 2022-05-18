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
    'title':'',
    'body':'',
    'head':'test/files',
    'base': 'test/pull'
}


def request_POST(url, data: Dict) -> Dict:
    """
    This function is only for requests with method post
    This functions is used when going to create a pull request
    with status open
    """
    try:
        response = requests.post(url, headers=HEADERS_GITHUB, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()
        return {'success': True, 'data': response_json}
    except Exception as e:
        error_response = {'success': False, 'message': str(e)}
        errors = response.json()
        print(errors)
        reason = errors['errors'][0].get('message', 'Error del administrador, se está revisando. Intentar más tarde.')
        error_response['reason'] = reason
        return error_response


def request_PUT(url: str) -> Dict:
    """
    This function is only for requests with method post
    This functions is used when going to create a pull request
    with status merge
    """
    try:
        response = requests.put(url, headers=HEADERS_GITHUB)
        response.raise_for_status()
        response_json = response.json()
        return {'success': True, 'data': response_json}
    except Exception as e:
        print(e)
        return {'success': False}


def request_GET(url) -> Dict:
    """
    This function is only for requests with method get
    This functions is used to get data to:
        - Commits
        - Branches
        - Authors (Collaborators)
    """
    try:
        response = requests.get(url, headers=HEADERS_GITHUB)
        response.raise_for_status()
        response_json = response.json()
        return {'success': True, 'data': response_json}
    except requests.exceptions.Timeout as to:
        print(to)
        return {'success': False, 'message': 'Proveedor no disponible por el momento. Intente más tarde'}
    except Exception as e:
        reason = response.json().get('message', 'Contactar con soporte')
        return {'success': False, 'message': str(e), 'reason':reason}


class HubManage(ABC):

    """
    This Abstract Class is set
    different methods to use with different
    providers (Github, Gitlab, etc)
    """

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

    """
    This class is for manage requests to GitHub
    Get Data or send data. Inheriting from HubManage
    """

    @classmethod
    def get_all_commit(cls) -> Dict:
        """
        This function is to get all commits from this repo
        """
        print("<------ Get All Commits ------>")
        url = f"{settings.GIT_URL}/commits"
        response_commits = request_GET(url)
        print(response_commits)
        if not response_commits:
            return None
        return response_commits

    @classmethod
    def get_commit_by_sha(cls, sha: str) -> Dict:
        """
        This function is to get details commits by sha
        """
        print("<------ Get Commit by Sha ------>")
        url = f"{settings.GIT_URL}/commits/{sha}"
        response_commit = request_GET(url)
        print(response_commit)
        return response_commit

    @classmethod
    def get_all_branches(cls) -> Dict:
        """
        This function is to get all branches from this repository
        """
        print("<------ Get All Branch ------>")
        url = f"{settings.GIT_URL}/branches"
        response_branches = request_GET(url)
        print(response_branches)
        if not response_branches:
            return None
        return response_branches

    @classmethod
    def get_branch_detail(cls, branch: str) -> Dict:
        """
        This function is to get details of a branch from this repository by name
        """
        print("<------ Get Branch Details ------>")
        url = f"{settings.GIT_URL}/branches/{branch}"
        response_branch= request_GET(url)
        print(response_branch)
        if not response_branch:
            return None
        return response_branch

    @classmethod
    def get_all_authors(cls) -> Dict:
        """
        This function is to get all authors (collaborators) from this repository
        """
        print("<------ GET All Authors ------>")
        url = f"{settings.GIT_URL}/collaborators"
        response_authors = request_GET(url)
        return response_authors


    @classmethod
    def get_all_pull_request(cls) -> Dict:
        """
        This function is to get all pull requests created for this repository
        """
        print("<------ Get Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls?state=all"
        response_pull= request_GET(url)
        print(response_pull)
        if not response_pull:
            return None
        return response_pull

    @classmethod
    def get_details_pull_request(cls, number: int) -> Dict:
        """
        This function is to get details of a pull request by number
        """
        print("<------ Get Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls/{number}"
        response_pull= request_GET(url)
        print(response_pull)
        if not response_pull:
            return None
        return response_pull


    @classmethod
    def create_pull_request(cls, data: Dict, branch_name: str=None) -> Dict:
        """
        This function is to create a pull requests with status open.
        Only we need send data and set url to function request_POST
        """
        print("<------ Create Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls"
        BODY_CREATE_PULL['title'] = data['title']
        BODY_CREATE_PULL['body'] = data['description']
        BODY_CREATE_PULL['head'] = branch_name or BODY_CREATE_PULL['head']
        response_pull = request_POST(url, BODY_CREATE_PULL)
        return response_pull


    @classmethod
    def merge_pull_request(cls, number: int):
        """
        This function is to create a pull requests with status merge.
        Only we need send data and set url to function request_PUT
        """
        print("<------ Merge Pull Request ------>")
        url = f"{settings.GIT_URL}/pulls/{number}/merge"
        response_pull = request_PUT(url)
        return response_pull


    @classmethod
    def send_push(cls, name_branch: str):
        """
        This function is to send a push to github using subproccess.
        """
        subprocess.run(f'git push repo {name_branch}', shell=True)


class CommitManage:

    """
    This class is to manage branchs, create documents for commits
    """

    @classmethod
    def create_branch(cls, name_branch: str) -> bool:
        """
        This function is to create a branch using subprocess with the shell
        """
        try:
            print(f'<------- Create Branch {name_branch} ------->')
            subprocess.run(f'git checkout -b {name_branch}', shell=True)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def create_document(cls) -> bool:
        """
        This function is to create a document for new commit using subprocess with the shell
        """
        print(f'<------- Create Document ------->')
        try:
            file_name = f'doc_{str(uuid.uuid4())[:4]+".txt"}'
            subprocess.run(f'touch {file_name}', shell=True)
            return {'success': True, 'file_name': file_name}
        except Exception as e:
            print(e)
            return {'success': False}


    @classmethod
    def create_commit(cls, file_name: str):
        """
        This function is to create a commit for send to github using subprocess with the shell
        """
        print(f'<------- Create Commit ------->')
        try:
            subprocess.run(f'git add {file_name} ; git commit -m "Test: Commit new file"', shell=True)
            return True
        except Exception as e:
            print(e)
            return False
