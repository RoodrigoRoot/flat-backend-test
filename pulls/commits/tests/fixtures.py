import pytest


@pytest.fixture()
def mock_all_commits():
    data = {'success':True, 'data':[
        {
            "sha": "113446b77e491aadd665ba56b0df96a86630e78d",
            "node_id": "C_kwDOHUgvcNoAKDExMzQ0NmI3N2U0OTFhYWRkNjY1YmE1NmIwZGY5NmE4NjYzMGU3OGQ",
            "commit": {
                "author": {
                    "name": "Rodrigo Urcino",
                    "email": "roodrigoroot@gmail.com",
                    "date": "2022-05-16T06:01:28Z"
                },
                "committer": {
                    "name": "GitHub",
                    "email": "noreply@github.com",
                    "date": "2022-05-16T06:01:28Z"
                },
                "message": "Merge pull request #50 from RoodrigoRoot/docs/readme_v2\n\nDocs/readme v2",
                "tree": {
                    "sha": "404514dc07ad16ee98ed24e14ab9f8dcfb56d3b0",
                    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/git/trees/404514dc07ad16ee98ed24e14ab9f8dcfb56d3b0"
                },
                "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/git/commits/113446b77e491aadd665ba56b0df96a86630e78d",
                "comment_count": 0,
                "verification": {
                    "verified": True,
                    "reason": "valid",
                    "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJigei4CRBK7hj4Ov3rIwAAKJoIAG4dqlmGMARZdq4Ehg/AKPZx\nTf36Pio+TirDY8ZWrHT1gqE/Vf7SHqOwN55ankILC7N+2PQKIKUlmgymiY7tflwI\nIEIlfGrgWMx2kEZx3Cm4tfjNDL8VqlbE5bhyKIxPl/T0bYLFN+GW65i4ecKv+3S8\nECidjLspp1tYLepgGZR+K9ufrpBhC22K/gwkgcEchwrb8V/KZih99HAvC6brEfeU\nLz8g1HZySy2LK2a1/GQYmQ5kI/iMk1pZ8Ak0n7H68OsSP6O9Y8maXvqVTUF1T0jn\nAU6fvBw1DDGiJO8Mn9E4qVisecYEeB6JU+eNfkkqj5diIOEagLx0lX0mRx+W+cE=\n=2ahn\n-----END PGP SIGNATURE-----\n",
                    "payload": "tree 404514dc07ad16ee98ed24e14ab9f8dcfb56d3b0\nparent e6b105e4b37a97227a3e91801ae6192684507648\nparent 92672a4afab2efc9fa5f948c81844a415ad4a22e\nauthor Rodrigo Urcino <roodrigoroot@gmail.com> 1652680888 -0500\ncommitter GitHub <noreply@github.com> 1652680888 -0500\n\nMerge pull request #50 from RoodrigoRoot/docs/readme_v2\n\nDocs/readme v2"
                }
            },
            "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/113446b77e491aadd665ba56b0df96a86630e78d",
            "html_url": "https://github.com/RoodrigoRoot/flat-backend-test/commit/113446b77e491aadd665ba56b0df96a86630e78d",
            "comments_url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/113446b77e491aadd665ba56b0df96a86630e78d/comments",
            "author": {
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
                "site_admin": False
            },
            "committer": {
                "login": "web-flow",
                "id": 19864447,
                "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/web-flow",
                "html_url": "https://github.com/web-flow",
                "followers_url": "https://api.github.com/users/web-flow/followers",
                "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                "organizations_url": "https://api.github.com/users/web-flow/orgs",
                "repos_url": "https://api.github.com/users/web-flow/repos",
                "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                "received_events_url": "https://api.github.com/users/web-flow/received_events",
                "type": "User",
                "site_admin": False
            },
            "parents": [
                {
                    "sha": "e6b105e4b37a97227a3e91801ae6192684507648",
                    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/e6b105e4b37a97227a3e91801ae6192684507648",
                    "html_url": "https://github.com/RoodrigoRoot/flat-backend-test/commit/e6b105e4b37a97227a3e91801ae6192684507648"
                },
                {
                    "sha": "92672a4afab2efc9fa5f948c81844a415ad4a22e",
                    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/92672a4afab2efc9fa5f948c81844a415ad4a22e",
                    "html_url": "https://github.com/RoodrigoRoot/flat-backend-test/commit/92672a4afab2efc9fa5f948c81844a415ad4a22e"
                }
            ]
        }
    ]}
    return data


@pytest.fixture
def mock_details_commit():
    data = {'success':True, 'data':{
        "sha": "113446b77e491aadd665ba56b0df96a86630e78d",
        "node_id": "C_kwDOHUgvcNoAKDExMzQ0NmI3N2U0OTFhYWRkNjY1YmE1NmIwZGY5NmE4NjYzMGU3OGQ",
        "commit": {
            "author": {
                "name": "Rodrigo Urcino",
                "email": "roodrigoroot@gmail.com",
                "date": "2022-05-16T06:01:28Z"
            },
            "committer": {
                "name": "GitHub",
                "email": "noreply@github.com",
                "date": "2022-05-16T06:01:28Z"
            },
            "message": "Merge pull request #50 from RoodrigoRoot/docs/readme_v2\n\nDocs/readme v2",
            "tree": {
                "sha": "404514dc07ad16ee98ed24e14ab9f8dcfb56d3b0",
                "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/git/trees/404514dc07ad16ee98ed24e14ab9f8dcfb56d3b0"
            },
            "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/git/commits/113446b77e491aadd665ba56b0df96a86630e78d",
            "comment_count": 0,
            "verification": {
                "verified": True,
                "reason": "valid",
                "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJigei4CRBK7hj4Ov3rIwAAKJoIAG4dqlmGMARZdq4Ehg/AKPZx\nTf36Pio+TirDY8ZWrHT1gqE/Vf7SHqOwN55ankILC7N+2PQKIKUlmgymiY7tflwI\nIEIlfGrgWMx2kEZx3Cm4tfjNDL8VqlbE5bhyKIxPl/T0bYLFN+GW65i4ecKv+3S8\nECidjLspp1tYLepgGZR+K9ufrpBhC22K/gwkgcEchwrb8V/KZih99HAvC6brEfeU\nLz8g1HZySy2LK2a1/GQYmQ5kI/iMk1pZ8Ak0n7H68OsSP6O9Y8maXvqVTUF1T0jn\nAU6fvBw1DDGiJO8Mn9E4qVisecYEeB6JU+eNfkkqj5diIOEagLx0lX0mRx+W+cE=\n=2ahn\n-----END PGP SIGNATURE-----\n",
                "payload": "tree 404514dc07ad16ee98ed24e14ab9f8dcfb56d3b0\nparent e6b105e4b37a97227a3e91801ae6192684507648\nparent 92672a4afab2efc9fa5f948c81844a415ad4a22e\nauthor Rodrigo Urcino <roodrigoroot@gmail.com> 1652680888 -0500\ncommitter GitHub <noreply@github.com> 1652680888 -0500\n\nMerge pull request #50 from RoodrigoRoot/docs/readme_v2\n\nDocs/readme v2"
            }
        },
        "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/113446b77e491aadd665ba56b0df96a86630e78d",
        "html_url": "https://github.com/RoodrigoRoot/flat-backend-test/commit/113446b77e491aadd665ba56b0df96a86630e78d",
        "comments_url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/113446b77e491aadd665ba56b0df96a86630e78d/comments",
        "author": {
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
            "site_admin": False
        },
        "committer": {
            "login": "web-flow",
            "id": 19864447,
            "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
            "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/web-flow",
            "html_url": "https://github.com/web-flow",
            "followers_url": "https://api.github.com/users/web-flow/followers",
            "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
            "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
            "organizations_url": "https://api.github.com/users/web-flow/orgs",
            "repos_url": "https://api.github.com/users/web-flow/repos",
            "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
            "received_events_url": "https://api.github.com/users/web-flow/received_events",
            "type": "User",
            "site_admin": False
        },
        "parents": [
            {
                "sha": "e6b105e4b37a97227a3e91801ae6192684507648",
                "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/e6b105e4b37a97227a3e91801ae6192684507648",
                "html_url": "https://github.com/RoodrigoRoot/flat-backend-test/commit/e6b105e4b37a97227a3e91801ae6192684507648"
            },
            {
                "sha": "92672a4afab2efc9fa5f948c81844a415ad4a22e",
                "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/92672a4afab2efc9fa5f948c81844a415ad4a22e",
                "html_url": "https://github.com/RoodrigoRoot/flat-backend-test/commit/92672a4afab2efc9fa5f948c81844a415ad4a22e"
            }
        ],
        "stats": {
            "total": 69,
            "additions": 63,
            "deletions": 6
        },
        "files": [
            {
                "sha": "d96a661ab2191b457b874ee7bec08f5e2a304f13",
                "filename": "README.md",
                "status": "modified",
                "additions": 63,
                "deletions": 6,
                "changes": 69,
                "blob_url": "https://github.com/RoodrigoRoot/flat-backend-test/blob/113446b77e491aadd665ba56b0df96a86630e78d/README.md",
                "raw_url": "https://github.com/RoodrigoRoot/flat-backend-test/raw/113446b77e491aadd665ba56b0df96a86630e78d/README.md",
                "contents_url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/contents/README.md?ref=113446b77e491aadd665ba56b0df96a86630e78d",
                "patch": "@@ -1,79 +1,136 @@\n-\n # This project is to technical interview of Flat.mx\n \n+\n ## Overview:\n+\n API Rest to get data from a repository, in this case we are going to retrive: Authors, Commits, Branches and Pull Request, using [GitHub Rst API v3](https://docs.github.com/en/rest)\n \n \n-## Objectives  \n+## Objectives\n+\n This project proposes a solution based on Api Rest based on this interview [Flat Digital Backend Interview](https://github.com/FlatDigital/backend-gitwrap-test)\n \n-## Use cases to support:  \n+\n+## Use cases to support:\n+\n - Anyone can use this project\n+\n - Create an API REST to:\n+\n - Create Pull Request\n+\n - Merge Pull Request\n+\n - Get all Pull Request\n+\n - Get details Pull Request\n+\n - Get all commits repository\n+\n - Get details commit\n+\n - Get all branches repository\n+\n - Get all authors repository\n \n+\n ## Use cases unsupported:\n+\n - Login for users\n--  Create users\n+\n+- Create users\n+\n - Save Commits on DB\n+\n - Save Branches on DB\n+\n - Delete Branches\n+\n - Delete Commits\n+\n - Delete Pull Request\n \n+\n ## Stack's technology\n+\n - Python\n+\n - Django\n+\n - PostgreSQL\n+\n - Docker\n+\n - Docker Compose\n+\n - Makefile\n \n+\n ## The structure this project is based on:\n+\n [Django StyleGuide from HackSoftware](https://github.com/HackSoftware/Django-Styleguide)\n+\n **with some changes**\n \n \n+## Instructions\n \n-## Instructions \n #### These instructions use [make](https://es.wikipedia.org/wiki/Make) to streamline interaction with the project.\n+\n > Note: If not had `make` on your compute at the bottom of this page are instructions with docker commands\n \n+\n ### To build and run project\n+\n **Build project**\n+\n `make build`\n \n+\n **Run project**\n+\n `make run`\n \n+\n #### To stop project\n+\n `make stop`\n \n+\n ## Other commands\n+\n #### To enter the inside of the container bash\n+\n `make bash`\n \n+\n #### To watch logs of Back\n+\n `make logs-back`\n \n+\n #### To watch logs of DB\n+\n `make logs-db`\n \n \n-## Instructions with Docker Compose  \n+## Instructions with Docker Compose\n+\n #### To run project\n+\n `docker-compose up`\n \n+\n #### To stop project\n+\n `docker-compose stop`\n \n+\n ## Documentation\n \n+For this project we use Swagger and postman\n+\n+[Collection of Postman](https://drive.google.com/file/d/1lCvnCTeXM9iQMwOxkzadjMJ6ULd1UDne/view?usp=sharing)\n+\n+With swagger we need run the project and go to '/api/v1/docs/'\n+[Swagger](http://localhost:8000/api/v1/docs/)\n\\ No newline at end of file"
            },
            {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "doc_61e1.txt",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/RoodrigoRoot/flat-backend-test/blob/113446b77e491aadd665ba56b0df96a86630e78d/doc_61e1.txt",
                "raw_url": "https://github.com/RoodrigoRoot/flat-backend-test/raw/113446b77e491aadd665ba56b0df96a86630e78d/doc_61e1.txt",
                "contents_url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/contents/doc_61e1.txt?ref=113446b77e491aadd665ba56b0df96a86630e78d"
            }
        ]
    }}
    return data
