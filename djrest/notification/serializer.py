from rest_framework import serializers
from .models import MessageLog


class MessageLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    text = serializers.CharField(read_only=True)
    date_sent = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Message` instance, given the validated data.
        """
        return MessageLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        """
        return instance
