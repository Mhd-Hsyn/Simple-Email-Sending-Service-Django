from django.urls import path
from .views import SendMessageToAdminsView

urlpatterns = [
    path('send-message/', SendMessageToAdminsView.as_view(), name='send-message-to-admins'),
]
