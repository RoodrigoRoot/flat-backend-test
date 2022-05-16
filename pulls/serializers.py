from cProfile import label
from random import choices
from rest_framework import serializers


class PullRequestSerializer(serializers.Serializer):

    url = serializers.URLField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=150)
    title = serializers.CharField(max_length=250)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    status = serializers.SerializerMethodField()
    number = serializers.IntegerField()

    def get_status(self, obj):
        return obj.get('state', '')


class CreatePullRequestSerializer(serializers.Serializer):

    STATUS_MERGE = {
        'open':'open',
        'merge':'merge'
    }

    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    status = serializers.ChoiceField(choices=STATUS_MERGE)

    def validate_status(self, status):
        if not status in self.STATUS_MERGE.keys():
            raise serializers.ValidationError('Please check status merge')
        return status
