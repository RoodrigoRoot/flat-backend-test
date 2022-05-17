# Get All Authors

Used to get all Authors for this repository

**URL** : `/api/v1/authors/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "name": "RoodrigoRoot",
    "url_profile": "https://github.com/RoodrigoRoot"
  }
]
```

# Get Commits

Used to get all Commits for this repository

**URL** : `/api/v1/commits/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "sha": "0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de",
    "commit": {
      "author": {
        "name": "Rodrigo",
        "email": "roodrigoroot@gmail.com",
        "date": "2022-05-17T19:51:29Z"
      },
      "message": "Chore: Delete files"
    },
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de"
  }
]
```

# Get All Commits

Used to get all Commits for this repository

**URL** : `/api/v1/commits/<sha:str>`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "sha": "0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de",
    "commit": {
      "author": {
        "name": "Rodrigo",
        "email": "roodrigoroot@gmail.com",
        "date": "2022-05-17T19:51:29Z"
      },
      "message": "Chore: Delete files"
    },
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de"
  }
]
```

# Get Details Commit

Used to get Details a Commit for this repository

**URL** : `/api/v1/commits/<sha:str>/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "sha": "0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de",
    "commit": {
      "author": {
        "name": "Rodrigo",
        "email": "roodrigoroot@gmail.com",
        "date": "2022-05-17T19:51:29Z"
      },
      "message": "Chore: Delete files"
    },
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de"
}

```



# Get Commits

Used to get all Commits for this repository

**URL** : `/api/v1/commits/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "sha": "0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de",
    "commit": {
      "author": {
        "name": "Rodrigo",
        "email": "roodrigoroot@gmail.com",
        "date": "2022-05-17T19:51:29Z"
      },
      "message": "Chore: Delete files"
    },
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de"
  }
]
```

# Get All Branches

Used to get all Branches for this repository

**URL** : `/api/v1/branches/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "name": "fix/branch",
    "protected": false
  },
  {
    "name": "main",
    "protected": false
  },
  {
    "name": "test/pull",
    "protected": false
  },
  {
    "name": "test/test_features",
    "protected": false
  }
]
```

# Get Details Branch

Used to get Details a Branch for this repository

**URL** : `/api/v1/branches/<branch:str>/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "name": "main",
  "commit": {
    "sha": "0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de",
    "commit": {
      "author": {
        "name": "Rodrigo",
        "email": "roodrigoroot@gmail.com",
        "date": "2022-05-17T19:51:29Z"
      },
      "message": "Chore: Delete files"
    },
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/0dce5fa98f4c6e355c1f144beac5b6c6fe9ea0de"
  }
}
```

# Get All Pull Request

Used to get All Pull Request for this repository

**URL** : `/api/v1/pulls/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/pulls/51",
    "id": 939204646,
    "title": "Test/test features",
    "created_at": "2022-05-17T19:41:04Z",
    "updated_at": "2022-05-17T19:41:21Z",
    "status": "closed",
    "number": 51
  },
  {
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/pulls/50",
    "id": 937063858,
    "title": "Docs/readme v2",
    "created_at": "2022-05-16T06:01:23Z",
    "updated_at": "2022-05-16T06:01:28Z",
    "status": "closed",
    "number": 50
  },
  {
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/pulls/49",
    "id": 937051141,
    "title": "prueba",
    "created_at": "2022-05-16T05:36:37Z",
    "updated_at": "2022-05-17T19:46:38Z",
    "status": "closed",
    "number": 49
  },
  {
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/pulls/48",
    "id": 937049592,
    "title": "Fix/branch",
    "created_at": "2022-05-16T05:33:15Z",
    "updated_at": "2022-05-16T05:33:20Z",
    "status": "closed",
    "number": 48
  }
]
```
# Get Details a Pull Request

Used to get Details Pull Request for this repository

**URL** : `/api/v1/pulls/<number:int>/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**


## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/pulls/51",
    "id": 939204646,
    "title": "Test/test features",
    "created_at": "2022-05-17T19:41:04Z",
    "updated_at": "2022-05-17T19:41:21Z",
    "status": "closed",
    "number": 51
}
```
# Create a Pull Request

Used to create a new stock on the database.

**URL** : `/api/v1/pulls/`

**Method** : `POST`

**Auth required** : NO

**Data example**

```json
{
  "title": "Pull de Prueba",
  "description": "Este Pull es de pruebas",
  "status": "open"
}
```

## Success Response

**Code** : `201 CREATED`

```json
{
        "url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/1347",
        "id": 1,
        "node_id": "MDExOlB1bGxSZXF1ZXN0MQ==",
        "html_url": "https://github.com/roodrigoroot/flat-backend-test/pull/1347",
        "diff_url": "https://github.com/roodrigoroot/flat-backend-test/pull/1347.diff",
        "patch_url": "https://github.com/roodrigoroot/flat-backend-test/pull/1347.patch",
        "issue_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/1347",
        "commits_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/1347/commits",
        "review_comments_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/1347/comments",
        "review_comment_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/comments{/number}",
        "comments_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/1347/comments",
        "statuses_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/statuses/6dcb09b5b57875f334f61aebed695e2e4193db5e",
        "number": 1347,
        "state": "open",
        "locked": True,
        "title": "Pull request de prueba",
        "user": {
            "login": "roodrigoroot",
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/roodrigoroot",
            "html_url": "https://github.com/roodrigoroot",
            "followers_url": "https://api.github.com/users/roodrigoroot/followers",
            "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
            "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
            "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
            "repos_url": "https://api.github.com/users/roodrigoroot/repos",
            "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
            "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
            "type": "User",
            "site_admin": False
        },
        "body": "Please pull these awesome changes in!",
        "labels": [
            {
                "id": 208045946,
                "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
                "url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/labels/bug",
                "name": "bug",
                "description": "Something isn't working",
                "color": "f29513",
                "default": True
            }
        ],
        "milestone": {
            "url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/milestones/1",
            "html_url": "https://github.com/roodrigoroot/flat-backend-test/milestones/v1.0",
            "labels_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/milestones/1/labels",
            "id": 1002604,
            "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
            "number": 1,
            "state": "open",
            "title": "v1.0",
            "description": "Tracking milestone for version 1.0",
            "creator": {
                "login": "roodrigoroot",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/roodrigoroot",
                "html_url": "https://github.com/roodrigoroot",
                "followers_url": "https://api.github.com/users/roodrigoroot/followers",
                "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
                "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
                "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
                "repos_url": "https://api.github.com/users/roodrigoroot/repos",
                "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
                "type": "User",
                "site_admin": False
            },
            "open_issues": 4,
            "closed_issues": 8,
            "created_at": "2011-04-10T20:09:31Z",
            "updated_at": "2014-03-03T18:58:10Z",
            "closed_at": "2013-02-12T13:22:01Z",
            "due_on": "2012-10-09T23:39:01Z"
        },
        "active_lock_reason": "too heated",
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2011-01-26T19:01:12Z",
        "closed_at": "2011-01-26T19:01:12Z",
        "merged_at": "2011-01-26T19:01:12Z",
        "merge_commit_sha": "e5bd3914e2e596debea16f433f57875b5b90bcd6",
        "assignee": {
            "login": "roodrigoroot",
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/roodrigoroot",
            "html_url": "https://github.com/roodrigoroot",
            "followers_url": "https://api.github.com/users/roodrigoroot/followers",
            "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
            "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
            "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
            "repos_url": "https://api.github.com/users/roodrigoroot/repos",
            "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
            "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
            "type": "User",
            "site_admin": False
        },
        "assignees": [
            {
                "login": "roodrigoroot",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/roodrigoroot",
                "html_url": "https://github.com/roodrigoroot",
                "followers_url": "https://api.github.com/users/roodrigoroot/followers",
                "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
                "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
                "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
                "repos_url": "https://api.github.com/users/roodrigoroot/repos",
                "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
                "type": "User",
                "site_admin": False
            },
            {
                "login": "hubot",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/hubot_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/hubot",
                "html_url": "https://github.com/hubot",
                "followers_url": "https://api.github.com/users/hubot/followers",
                "following_url": "https://api.github.com/users/hubot/following{/other_user}",
                "gists_url": "https://api.github.com/users/hubot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/hubot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/hubot/subscriptions",
                "organizations_url": "https://api.github.com/users/hubot/orgs",
                "repos_url": "https://api.github.com/users/hubot/repos",
                "events_url": "https://api.github.com/users/hubot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/hubot/received_events",
                "type": "User",
                "site_admin": True
            }
        ],
        "requested_reviewers": [
            {
                "login": "other_user",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/other_user_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/other_user",
                "html_url": "https://github.com/other_user",
                "followers_url": "https://api.github.com/users/other_user/followers",
                "following_url": "https://api.github.com/users/other_user/following{/other_user}",
                "gists_url": "https://api.github.com/users/other_user/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/other_user/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/other_user/subscriptions",
                "organizations_url": "https://api.github.com/users/other_user/orgs",
                "repos_url": "https://api.github.com/users/other_user/repos",
                "events_url": "https://api.github.com/users/other_user/events{/privacy}",
                "received_events_url": "https://api.github.com/users/other_user/received_events",
                "type": "User",
                "site_admin": False
            }
        ],
        "requested_teams": [
            {
                "id": 1,
                "node_id": "MDQ6VGVhbTE=",
                "url": "https://api.github.com/teams/1",
                "html_url": "https://github.com/orgs/github/teams/justice-league",
                "name": "Justice League",
                "slug": "justice-league",
                "description": "A great team.",
                "privacy": "closed",
                "permission": "admin",
                "members_url": "https://api.github.com/teams/1/members{/member}",
                "repositories_url": "https://api.github.com/teams/1/repos"
            }
        ],
        "head": {
            "label": "roodrigoroot:new-topic",
            "ref": "new-topic",
            "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
            "user": {
                "login": "roodrigoroot",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/roodrigoroot",
                "html_url": "https://github.com/roodrigoroot",
                "followers_url": "https://api.github.com/users/roodrigoroot/followers",
                "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
                "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
                "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
                "repos_url": "https://api.github.com/users/roodrigoroot/repos",
                "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
                "type": "User",
                "site_admin": False
            },
            "repo": {
                "id": 1296269,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
                "name": "flat-backend-test",
                "full_name": "roodrigoroot/flat-backend-test",
                "owner": {
                    "login": "roodrigoroot",
                    "id": 1,
                    "node_id": "MDQ6VXNlcjE=",
                    "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/roodrigoroot",
                    "html_url": "https://github.com/roodrigoroot",
                    "followers_url": "https://api.github.com/users/roodrigoroot/followers",
                    "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
                    "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
                    "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
                    "repos_url": "https://api.github.com/users/roodrigoroot/repos",
                    "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "private": False,
                "html_url": "https://github.com/roodrigoroot/flat-backend-test",
                "description": "This your first repo!",
                "fork": False,
                "url": "https://api.github.com/repos/roodrigoroot/flat-backend-test",
                "archive_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/{archive_format}{/ref}",
                "assignees_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/assignees{/user}",
                "blobs_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/blobs{/sha}",
                "branches_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/branches{/branch}",
                "collaborators_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/collaborators{/collaborator}",
                "comments_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/comments{/number}",
                "commits_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/commits{/sha}",
                "compare_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/compare/{base}...{head}",
                "contents_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/contents/{+path}",
                "contributors_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/contributors",
                "deployments_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/deployments",
                "downloads_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/downloads",
                "events_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/events",
                "forks_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/forks",
                "git_commits_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/commits{/sha}",
                "git_refs_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/refs{/sha}",
                "git_tags_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/tags{/sha}",
                "git_url": "git:github.com/roodrigoroot/flat-backend-test.git",
                "issue_comment_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/comments{/number}",
                "issue_events_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/events{/number}",
                "issues_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues{/number}",
                "keys_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/keys{/key_id}",
                "labels_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/labels{/name}",
                "languages_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/languages",
                "merges_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/merges",
                "milestones_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/notifications{?since,all,participating}",
                "pulls_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls{/number}",
                "releases_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/releases{/id}",
                "ssh_url": "git@github.com:roodrigoroot/flat-backend-test.git",
                "stargazers_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/stargazers",
                "statuses_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/statuses/{sha}",
                "subscribers_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/subscribers",
                "subscription_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/subscription",
                "tags_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/tags",
                "teams_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/teams",
                "trees_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/trees{/sha}",
                "clone_url": "https://github.com/roodrigoroot/flat-backend-test.git",
                "mirror_url": "git:git.example.com/roodrigoroot/flat-backend-test",
                "hooks_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/hooks",
                "svn_url": "https://svn.github.com/roodrigoroot/flat-backend-test",
                "homepage": "https://github.com",
                "language": None,
                "forks_count": 9,
                "stargazers_count": 80,
                "watchers_count": 80,
                "size": 108,
                "default_branch": "master",
                "open_issues_count": 0,
                "topics": [
                    "roodrigoroot",
                    "atom",
                    "electron",
                    "api"
                ],
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True,
                "has_pages": False,
                "has_downloads": True,
                "archived": False,
                "disabled": False,
                "pushed_at": "2011-01-26T19:06:43Z",
                "created_at": "2011-01-26T19:01:12Z",
                "updated_at": "2011-01-26T19:14:43Z",
                "permissions": {
                    "admin": False,
                    "push": False,
                    "pull": True
                },
                "allow_rebase_merge": True,
                "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
                "allow_squash_merge": True,
                "allow_merge_commit": True,
                "allow_forking": True,
                "forks": 123,
                "open_issues": 123,
                "license": {
                    "key": "mit",
                    "name": "MIT License",
                    "url": "https://api.github.com/licenses/mit",
                    "spdx_id": "MIT",
                    "node_id": "MDc6TGljZW5zZW1pdA=="
                },
                "watchers": 123
            }
        },
        "base": {
            "label": "roodrigoroot:master",
            "ref": "master",
            "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
            "user": {
                "login": "roodrigoroot",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/roodrigoroot",
                "html_url": "https://github.com/roodrigoroot",
                "followers_url": "https://api.github.com/users/roodrigoroot/followers",
                "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
                "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
                "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
                "repos_url": "https://api.github.com/users/roodrigoroot/repos",
                "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
                "type": "User",
                "site_admin": False
            },
            "repo": {
                "id": 1296269,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
                "name": "flat-backend-test",
                "full_name": "roodrigoroot/flat-backend-test",
                "owner": {
                    "login": "roodrigoroot",
                    "id": 1,
                    "node_id": "MDQ6VXNlcjE=",
                    "avatar_url": "https://github.com/images/error/roodrigoroot_happy.gif",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/roodrigoroot",
                    "html_url": "https://github.com/roodrigoroot",
                    "followers_url": "https://api.github.com/users/roodrigoroot/followers",
                    "following_url": "https://api.github.com/users/roodrigoroot/following{/other_user}",
                    "gists_url": "https://api.github.com/users/roodrigoroot/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/roodrigoroot/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/roodrigoroot/subscriptions",
                    "organizations_url": "https://api.github.com/users/roodrigoroot/orgs",
                    "repos_url": "https://api.github.com/users/roodrigoroot/repos",
                    "events_url": "https://api.github.com/users/roodrigoroot/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/roodrigoroot/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "private": False,
                "html_url": "https://github.com/roodrigoroot/flat-backend-test",
                "description": "This your first repo!",
                "fork": False,
                "url": "https://api.github.com/repos/roodrigoroot/flat-backend-test",
                "archive_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/{archive_format}{/ref}",
                "assignees_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/assignees{/user}",
                "blobs_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/blobs{/sha}",
                "branches_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/branches{/branch}",
                "collaborators_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/collaborators{/collaborator}",
                "comments_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/comments{/number}",
                "commits_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/commits{/sha}",
                "compare_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/compare/{base}...{head}",
                "contents_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/contents/{+path}",
                "contributors_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/contributors",
                "deployments_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/deployments",
                "downloads_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/downloads",
                "events_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/events",
                "forks_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/forks",
                "git_commits_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/commits{/sha}",
                "git_refs_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/refs{/sha}",
                "git_tags_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/tags{/sha}",
                "git_url": "git:github.com/roodrigoroot/flat-backend-test.git",
                "issue_comment_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/comments{/number}",
                "issue_events_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/events{/number}",
                "issues_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues{/number}",
                "keys_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/keys{/key_id}",
                "labels_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/labels{/name}",
                "languages_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/languages",
                "merges_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/merges",
                "milestones_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/notifications{?since,all,participating}",
                "pulls_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls{/number}",
                "releases_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/releases{/id}",
                "ssh_url": "git@github.com:roodrigoroot/flat-backend-test.git",
                "stargazers_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/stargazers",
                "statuses_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/statuses/{sha}",
                "subscribers_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/subscribers",
                "subscription_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/subscription",
                "tags_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/tags",
                "teams_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/teams",
                "trees_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/git/trees{/sha}",
                "clone_url": "https://github.com/roodrigoroot/flat-backend-test.git",
                "mirror_url": "git:git.example.com/roodrigoroot/flat-backend-test",
                "hooks_url": "https://api.github.com/repos/roodrigoroot/flat-backend-test/hooks",
                "svn_url": "https://svn.github.com/roodrigoroot/flat-backend-test",
                "homepage": "https://github.com",
                "language": None,
                "forks_count": 9,
                "stargazers_count": 80,
                "watchers_count": 80,
                "size": 108,
                "default_branch": "master",
                "open_issues_count": 0,
                "topics": [
                    "roodrigoroot",
                    "atom",
                    "electron",
                    "api"
                ],
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True,
                "has_pages": False,
                "has_downloads": True,
                "archived": False,
                "disabled": False,
                "pushed_at": "2011-01-26T19:06:43Z",
                "created_at": "2011-01-26T19:01:12Z",
                "updated_at": "2011-01-26T19:14:43Z",
                "permissions": {
                    "admin": False,
                    "push": False,
                    "pull": True
                },
                "allow_rebase_merge": True,
                "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
                "allow_squash_merge": True,
                "allow_merge_commit": True,
                "forks": 123,
                "open_issues": 123,
                "license": {
                    "key": "mit",
                    "name": "MIT License",
                    "url": "https://api.github.com/licenses/mit",
                    "spdx_id": "MIT",
                    "node_id": "MDc6TGljZW5zZW1pdA=="
                },
                "watchers": 123
            }
        },
        "_links": {
            "self": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/1347"
            },
            "html": {
                "href": "https://github.com/roodrigoroot/flat-backend-test/pull/1347"
            },
            "issue": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/1347"
            },
            "comments": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/issues/1347/comments"
            },
            "review_comments": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/1347/comments"
            },
            "review_comment": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/comments{/number}"
            },
            "commits": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/pulls/1347/commits"
            },
            "statuses": {
                "href": "https://api.github.com/repos/roodrigoroot/flat-backend-test/statuses/6dcb09b5b57875f334f61aebed695e2e4193db5e"
            }
        }
```





**Content example**


## Error Response

**Code** : `400 BAD REQUEST`

**Conditions**
* `title` field has content.
* `description` field has content.
* `status` field has content.

```json
{
  "title": [
    "Este campo es requerido."
  ],
  "description": [
    "Este campo es requerido."
  ],
  "status": [
    "Este campo es requerido."
  ]
}

```

**Code** : `400 BAD REQUEST`

**Conditions**
* `status` field must be open or merge

```json
{
  "status": [
    "\"other value\" no es una elección válida."
  ]
}

```
