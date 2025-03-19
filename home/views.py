from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdminEmail, MessageRecord
from .serializers import MessageRecordSerializer
from core.utils import send_message_to_admins

class SendMessageToAdminsView(APIView):
    def post(self, request):
        serializer = MessageRecordSerializer(data=request.data)
        if serializer.is_valid():
            message_obj = serializer.save()
            admin_emails = list(AdminEmail.objects.filter(is_active=True).values_list('email', flat=True))
            if admin_emails:
                send_message_to_admins(admin_emails, message_obj)
                message_obj.is_send = True
                message_obj.save()
                return Response({'message': 'Emails sent successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'No active admins found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
