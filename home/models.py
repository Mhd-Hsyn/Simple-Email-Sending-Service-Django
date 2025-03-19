from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class AdminEmail(BaseModel):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.email

class MessageRecord(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=30)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    