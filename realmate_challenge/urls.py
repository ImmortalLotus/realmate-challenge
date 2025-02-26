from django.urls import path
from .views import WebhookView,ConversationDetailsView,ConversationListView

urlpatterns = [
    path('webhook/', WebhookView.as_view(), name='webhook'),
    path('conversations/<uuid:id>/', ConversationDetailsView.as_view(), name='conversation-detail'),
    path('conversations/', ConversationListView.as_view(), name='conversations')
]
