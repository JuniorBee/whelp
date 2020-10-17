from rest_framework import serializers
from core.models import File


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)


class FileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'timestamp')
