from rest_framework import serializers


class AllAuthorsSerializer(serializers.Serializer):

    name = serializers.SerializerMethodField()
    url_profile = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.get('login', '')

    def get_url_profile(self, obj):
        return obj.get('html_url', '')