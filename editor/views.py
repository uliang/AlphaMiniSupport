from datetime import timedelta
from django.utils import timezone 
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView, exception_handler

from apiservice.models import Message
from apiservice.serializers import MessageSerializer

# Create your views here.

class MessageEditor(APIView) : 
    renderer_classes = [TemplateHTMLRenderer] 
    template_name = 'editor/editor.html'
    queryset = Message.objects.all()

    def handle_exception(self, exc):
        response = exception_handler(exc, context={})
        if response.status_code in [401, 403]: 
            return Response(data={}, status=response.status_code, 
                            template_name='account/login-required.html')
        return Response(data={}, status=response.status_code, 
                        template_name='account/error.html')

    def get_queryset(self) : 
        return self.queryset

    def get(self, request): 
        if not Message.objects.exists(): 
            new_message = Message(
                message="Good morning, how are you!",
                message_start= timezone.now().time(), 
                frequency=timedelta(minutes=30))
            new_message.save()
        message = self.get_queryset()[0]
        serializer = MessageSerializer(message, context={'request': request}) 
        return Response({
            'serializer': serializer, 
            'message': message })

    def post(self, request) : 
        message = self.get_queryset()[0]
        serializer = MessageSerializer(message, data=request.data, context={'request':request})
        if not serializer.is_valid(): 
            return Response({
                'serializer': serializer, 
                'message': message
            }) 

        serializer.save()
        return redirect('message-editor')

def index(request) : 
    return render(request, 'editor/index.html')