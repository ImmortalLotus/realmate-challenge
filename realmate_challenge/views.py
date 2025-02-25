from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers.webhook_serializer import WebhookSerializer
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