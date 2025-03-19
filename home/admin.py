from django.contrib import admin
from .models import AdminEmail, MessageRecord

# Register your models here.
admin.site.register(AdminEmail)
admin.site.register(MessageRecord)