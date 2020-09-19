from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from apiservice.models import Message
from apiservice.serializers import MessageSerializer

# Create your views here.


class MessageEditor(APIView) : 
    renderer_classes = [TemplateHTMLRenderer] 
    template_name = 'editor/editor.html'
    queryset = Message.objects.all()

    def get_queryset(self) : 
        return self.queryset

    def get(self, request): 
        if request.user.is_authenticated: 
            message = self.get_queryset()[0]
            serializer = MessageSerializer(message, context={'request': request}) 
            return Response({
                'serializer': serializer, 
                'message': message })
        return redirect('index')

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