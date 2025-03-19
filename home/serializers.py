from rest_framework import serializers
from .models import MessageRecord

class MessageRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRecord
        fields = ['name', 'email', 'phone', 'subject', 'body']
