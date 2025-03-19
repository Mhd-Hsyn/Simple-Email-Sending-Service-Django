from django.contrib import admin
from .models import AdminEmail, MessageRecord

# Register your models here.
@admin.register(AdminEmail)
class AdminEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('email',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20
    save_on_top = True
    fieldsets = (
        ('Basic Information', {
            'fields': ('email', 'is_active', 'first_name', 'last_name')
        }),
    )
    # readonly_fields = ('created_at', 'updated_at')

@admin.register(MessageRecord)
class MessageRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'body', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'body')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20
    save_on_top = True