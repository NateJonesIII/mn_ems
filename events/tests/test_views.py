# events/tests/test_views.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

@pytest.mark.django_db
def test_event_list_view():
    client = Client()
    response = client.get(reverse('event_list'))
    assert response.status_code == 200
    assert b'All Events' in response.content
