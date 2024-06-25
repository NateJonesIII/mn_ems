# accounts/tests/test_views.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client,TestCase


"""
@pytest.mark.django_db
def test_profile_view():
    user = User.objects.create_user(username='testuser', password='password123')
    client = Client()
    client.login(username='testuser', password='password123')
    response = client.get(reverse('user_profile'))
    assert response.status_code == 200
    assert b'Profile' in response.content
    assert b'testuser' in response.content
"""

class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')