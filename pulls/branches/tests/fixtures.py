import pytest


@pytest.fixture()
def mock_all_branches():
    data = {'success': True, 'data':[
        {
            "name": "branch_b856",
            "commit": {
                "sha": "7513600a20c2913a326c945ddcd2fc234b848441",
                "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/7513600a20c2913a326c945ddcd2fc234b848441"
            },
            "protected": False
        },
        {
            "name": "branch_d6ba",
            "commit": {
                "sha": "b5c5b678aad30675bc5ca22d02b7a62ca9d202c8",
                "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/b5c5b678aad30675bc5ca22d02b7a62ca9d202c8"
            },
            "protected": False
        }
    ]}
    return data


@pytest.fixture
def mock_detail_branch():
    data = {'success': True, 'data':{
        "name": "main",
        "commit": {
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
        },
        "_links": {
            "self": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/branches/main",
            "html": "https://github.com/RoodrigoRoot/flat-backend-test/tree/main"
        },
        "protected": False,
        "protection": {
            "enabled": False,
            "required_status_checks": {
                "enforcement_level": "off",
                "contexts": [

                ],
                "checks": [

                ]
            }
        },
        "protection_url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/branches/main/protection"
    }}
    return data
