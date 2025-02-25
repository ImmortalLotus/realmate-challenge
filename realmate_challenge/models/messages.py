
from django.db import models
import uuid
from .conversations import Conversations
class MessageStatusEnum(models.TextChoices):
    RECEIVED = 'RECEIVED'
    SENT = 'SENT'

class Messages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    direction = models.CharField(
            max_length=9,
            choices=MessageStatusEnum.choices,
            default=MessageStatusEnum.SENT,
        )
    content= models.TextField()
    conversation=models.ForeignKey(Conversations,on_delete=models.RESTRICT)#ninguém disse a regra. sempre assumir menos risco.
    timestamp=models.DateTimeField()