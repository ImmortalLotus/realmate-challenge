from rest_framework import serializers
from ..models.conversations import Conversations

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = ['status', 'open_date', 'close_date', 'id']
