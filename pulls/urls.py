from django.urls import path
from pulls.views import (AllCommitsAPIView, AllBranchesAPIView,
DetailCommitsAPIView, DetailsBranchAPIView, AllAuthorsAPIView, PullRequestAPIView,
DetailsPullRequestAPIView)


urlpatterns = [
    path('commits/', AllCommitsAPIView.as_view(), name="all_commits"),
    path('commits/<str:sha>/', DetailCommitsAPIView.as_view(), name="details_commit"),
    path('branches/', AllBranchesAPIView.as_view(), name="all_branches"),
    path('branches/<str:branch>/', DetailsBranchAPIView.as_view(), name="details_branch"),
    path('authors/', AllAuthorsAPIView.as_view(), name="all_authors"),
    path('pulls/', PullRequestAPIView.as_view(), name="all_pulls"),
    path('pulls/<int:number>/', DetailsPullRequestAPIView.as_view(), name="details_pull"),
]
