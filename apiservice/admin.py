from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import Message

# Register your models here.

admin.site.register(Message)

TokenAdmin.raw_id_fields = ['user']