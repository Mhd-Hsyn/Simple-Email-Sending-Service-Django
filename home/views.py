from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdminEmail, MessageRecord
from .serializers import MessageRecordSerializer
from core.utils import send_message_to_admin

class SendMessageToAdminsView(APIView):
    def post(self, request):
        serializer = MessageRecordSerializer(data=request.data)
        if serializer.is_valid():
            message_obj = serializer.save()
            active_admins = AdminEmail.objects.filter(is_active=True)
            for admin in active_admins:
                send_message_to_admin(admin.email, message_obj)
            message_obj.is_send = True
            message_obj.save()
            return Response({'message': 'Emails sent successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
