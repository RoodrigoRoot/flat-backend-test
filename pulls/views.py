from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from Utils.repo import GitHubManage
from pulls.commits.serializers import AllCommitsSerializer, DetailsCommitSerializer
from pulls.branches.serializers import AllBranchesSerializer, DetailBranchSerializer
from pulls.authors.serializers import AllAuthorsSerializer
from pulls.serializers import PullRequestSerializer, CreatePullRequestSerializer
from pulls.services import create_pull_request, merge_pull_request
# Create your views here.


class AllCommitsAPIView(APIView):

    @swagger_auto_schema(operation_description='Get all repository commits')
    def get(self, request, *args, **kwargs):
        commits = GitHubManage.get_all_commit()
        if not commits['success']:
            return Response(commits, status=status.HTTP_400_BAD_REQUEST)
        commits_serializer = AllCommitsSerializer(commits['data'], many=True)
        return Response(commits_serializer.data, status=status.HTTP_200_OK)


class DetailCommitsAPIView(APIView):

    @swagger_auto_schema(operation_description='Get details a commit')
    def get(self, request, *args, **kwargs):
        sha_commit = self.kwargs.get('sha', '')
        if not sha_commit:
            return Response({'success': False, 'message': "No se envió el campo sha"}, status=status.HTTP_400_BAD_REQUEST)
        commit_detail = GitHubManage.get_commit_by_sha(sha_commit)
        if not commit_detail['success']:
            return Response(commit_detail, status=status.HTTP_400_BAD_REQUEST)
        commit_detail_serializer = DetailsCommitSerializer(commit_detail['data'])
        return Response(commit_detail_serializer.data, status=status.HTTP_200_OK)


class AllBranchesAPIView(APIView):

    @swagger_auto_schema(operation_description='Get all repository branches')
    def get(self, request, *args, **kwargs):
        branches = GitHubManage.get_all_branches()
        if not branches['success']:
            return Response(branches, status=status.HTTP_400_BAD_REQUEST)
        branches_serializers = AllBranchesSerializer(branches['data'], many=True)
        return Response(branches_serializers.data, status=status.HTTP_200_OK)


class DetailsBranchAPIView(APIView):

    @swagger_auto_schema(operation_description='Get details a branch')
    def get(self, request, *args, **kwargs):
        branch_name = self.kwargs.get('branch', '')
        if not branch_name:
            return Response({'success': False, 'message': "No se envió el nombre de la rama"}, status=status.HTTP_400_BAD_REQUEST)
        branch = GitHubManage.get_branch_detail(branch_name)
        if not branch['success']:
            return Response(branch, status=status.HTTP_400_BAD_REQUEST)
        branch_serializer = DetailBranchSerializer(branch['data'])
        return Response(branch_serializer.data, status=status.HTTP_200_OK)


class AllAuthorsAPIView(APIView):

    @swagger_auto_schema(operation_description='Get all repository authors')
    def get(self, request, *args, **kwargs):
        authors = GitHubManage.get_all_authors()
        if not authors['success']:
            return Response(authors, status=status.HTTP_400_BAD_REQUEST)
        authors_serializer = AllAuthorsSerializer(authors['data'], many=True)
        return Response(authors_serializer.data, status=status.HTTP_200_OK)


class PullRequestAPIView(APIView):

    @swagger_auto_schema(operation_description='Get all pulls requests')
    def get(self, request, *args, **kwargs):
        all_pull_request = GitHubManage.get_all_pull_request()
        serializer_pulls = PullRequestSerializer(all_pull_request['data'], many=True)
        return Response(serializer_pulls.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description='Create a pull request', request_body=CreatePullRequestSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CreatePullRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_pull_request = serializer.validated_data.get('status', '')
        if status_pull_request == 'merge':
            response = merge_pull_request(serializer.data)
        else:
            response = create_pull_request(serializer.data)
        if not response['success']:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_201_CREATED)


class DetailsPullRequestAPIView(APIView):

    @swagger_auto_schema(operation_description='Get details a pull request')
    def get(self, request, *args, **kwargs):
        number = self.kwargs.get('number', '')
        if not number:
            return Response({'success': False, 'message': "No se envió el campo number"}, status=status.HTTP_400_BAD_REQUEST)
        pull_request = GitHubManage.get_details_pull_request(number)
        if not pull_request['success']:
            return Response(pull_request, status=status.HTTP_400_BAD_REQUEST)
        serializer_pull = PullRequestSerializer(pull_request['data'])
        return Response(serializer_pull.data, status=status.HTTP_200_OK)
