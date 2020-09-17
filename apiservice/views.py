from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MessageSerializer
from .models import Message

# Create your views here.


class MessageViewSet(viewsets.ModelViewSet) : 
    queryset = Message.objects.all().order_by('-updated_on')
    serializer_class = MessageSerializer 
    permission_classes = [permissions.DjangoModelPermissions, 
                          permissions.IsAuthenticated]
