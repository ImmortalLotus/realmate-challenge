from rest_framework import serializers
from ..models.messages import Messages

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'direction', 'content', 'conversation', 'timestamp']