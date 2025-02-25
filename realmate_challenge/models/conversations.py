from django.db import models
import uuid

class ConversationStatusEnum(models.TextChoices):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'

class Conversations(models.Model):
    status = models.CharField(
        max_length=6,
        choices=ConversationStatusEnum.choices,
        default=ConversationStatusEnum.OPEN, 
    )
    open_date = models.DateTimeField()#eu não quero ter que lidar com a falta de histórico depois de meses de projeto. 
    close_date = models.DateTimeField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


