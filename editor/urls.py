from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index') , 
    path('editor/', views.MessageEditor.as_view(), name='message-editor')
]