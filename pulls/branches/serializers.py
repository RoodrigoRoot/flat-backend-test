from rest_framework import serializers
from pulls.commits.serializers import DetailsCommitSerializer


class AllBranchesSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    protected = serializers.BooleanField()


class DetailBranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    commit = DetailsCommitSerializer()

