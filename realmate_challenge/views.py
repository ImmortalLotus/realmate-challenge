from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers.webhook_serializer import WebhookSerializer
from .models.conversations import Conversations
from .models.messages import Messages
from .serializers.messages_serializer import MessageSerializer
from .serializers.conversations_serializer import ConversationSerializer
import logging

logger = logging.getLogger('django')

class WebhookView(APIView):
    def post(self, request):
        try:
            serializer = WebhookSerializer(data=request.data)
            logger.info(serializer)
            if serializer.is_valid():
                event = serializer.treat_webhook(serializer.validated_data)
        except Exception as e: 
            logger.error(f"Unexpected error: {e}",exc_info=True)
        finally:
            #a api oficial do whatsapp não se importa com corpo de retorno. 
            return Response(status=200)

class ConversationDetailsView(APIView):
    def get(self, request, id):
        try: 
            conversation = Conversations.objects.get(id=id)
        except Conversations.DoesNotExist:
            raise Exception("This conversation does not exist")

        messages = Messages.objects.filter(conversation=conversation).order_by('timestamp')

        serializer = MessageSerializer(messages, many=True)

        return Response({
            "conversation_id": conversation.id,
            "status": conversation.status,
            "messages": serializer.data
        }, status=200)

class ConversationListView(APIView):
    def get(self, request):
        conversations = Conversations.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=200)
