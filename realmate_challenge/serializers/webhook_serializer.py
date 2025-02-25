from rest_framework import serializers
from .messages_serializer import MessageSerializer
from .conversations_serializer import ConversationSerializer
from ..models.conversations import Conversations
import uuid
import logging

logger = logging.getLogger('django')

class WebhookSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=["NEW_CONVERSATION", "NEW_MESSAGE","CLOSE_CONVERSATION"])
    timestamp = serializers.DateTimeField()
    data = serializers.JSONField()
    def treat_webhook(self, validated_data):
        event_type = validated_data['type']
        data = validated_data['data']
        if event_type == 'NEW_CONVERSATION':
            # Create new conversation
            conversation_data = {
                'id': uuid.UUID(data['id']),
                'status': 'OPEN',  # Default status
                'open_date': validated_data['timestamp'],
                'close_date': None  # You can set this based on your logic
            }
            conversation_serializer = ConversationSerializer(data=conversation_data)
            conversation_serializer.is_valid(raise_exception=True)
            conversation = conversation_serializer.save()

            return conversation

        elif event_type == 'NEW_MESSAGE':


            conversation_id = uuid.UUID(data['conversation_id'])
            try: 
                conversation = Conversations.objects.get(id=conversation_id)
            except Conversations.DoesNotExist:
                raise Exception("This message is trying to append itself to a non-existing conversation")

            if conversation.status=='CLOSED':
                raise Exception("This conversation is closed.")
            message_data = {
                'id': uuid.UUID(data['id']),
                'direction': data['direction'],
                'content': data['content'],
                'conversation': uuid.UUID(data['conversation_id']),
                'timestamp': validated_data['timestamp']
            }
            message_serializer = MessageSerializer(data=message_data)
            message_serializer.is_valid(raise_exception=True)
            message = message_serializer.save()

            return message
        
        elif event_type == 'CLOSE_CONVERSATION':
            conversation_id = uuid.UUID(data['id'])
            try:
                conversation = Conversations.objects.get(id=conversation_id)
                logger.info(conversation)
                conversation.status = 'CLOSED'
                conversation.close_date = validated_data['timestamp']
                conversation.save()
                return conversation
            except Conversations.DoesNotExist:
                raise serializers.ValidationError("Conversation not found.")