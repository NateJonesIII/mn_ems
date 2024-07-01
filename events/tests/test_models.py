# events/tests/test_models.py

import pytest
from events.models import Event

@pytest.mark.django_db
def test_event_str():
    event = Event.objects.create(title='Test Event', date='2024-06-23')
    assert str(event) == 'Test Event'
