from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from apiservice.models import Message
# Create your tests here.

class TestEditor(TestCase): 

    def setUp(self) : 
        self.user = User.objects.create_user("john", "", "abc123")

    def test_login_to_editor_without_initail_message(self) :
        self.client.post(reverse('login'), data={'username': 'john', 'password': 'abc123'})
        response = self.client.get(reverse('message-editor'))
        self.assertContains(response, 'john')
        self.assertContains(response, 'Good morning, how are you!')