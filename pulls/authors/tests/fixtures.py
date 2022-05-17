import pytest


@pytest.fixture
def mock_authors():
    data = {'success':True, 'data':[
        {
            "login": "RoodrigoRoot",
            "id": 50676016,
            "node_id": "MDQ6VXNlcjUwNjc2MDE2",
            "avatar_url": "https://avatars.githubusercontent.com/u/50676016?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/RoodrigoRoot",
            "html_url": "https://github.com/RoodrigoRoot",
            "followers_url": "https://api.github.com/users/RoodrigoRoot/followers",
            "following_url": "https://api.github.com/users/RoodrigoRoot/following{/other_user}",
            "gists_url": "https://api.github.com/users/RoodrigoRoot/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/RoodrigoRoot/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/RoodrigoRoot/subscriptions",
            "organizations_url": "https://api.github.com/users/RoodrigoRoot/orgs",
            "repos_url": "https://api.github.com/users/RoodrigoRoot/repos",
            "events_url": "https://api.github.com/users/RoodrigoRoot/events{/privacy}",
            "received_events_url": "https://api.github.com/users/RoodrigoRoot/received_events",
            "type": "User",
            "site_admin": False,
            "permissions": {
                "admin": True,
                "maintain": True,
                "push": True,
                "triage": True,
                "pull": True
            },
            "role_name": "admin"
        }
    ]}
    return data
