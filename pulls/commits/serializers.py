from abc import ABC, ABCMeta
from rest_framework import serializers




class CommitAuthorSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=250)
    date = serializers.DateTimeField()


class CommitSerializer(serializers.Serializer):

    author = CommitAuthorSerializer()
    message = serializers.CharField(max_length=150)

class AbstractCommitsSerializer(serializers.Serializer):
    sha = serializers.CharField(max_length=150)
    commit = CommitSerializer()
    url = serializers.URLField()


    class Meta:
        abstract = True

class DetailsCommitSerializer(AbstractCommitsSerializer):
    ...


class AllCommitsSerializer(AbstractCommitsSerializer):
    ...

    def validate(self, attrs):
        if type(attrs) == dict:
            return []

