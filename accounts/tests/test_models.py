# accounts/tests/test_models.py

import pytest
from django.contrib.auth.models import User
from accounts.models import Profile

@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create_user(username='testuser', password='password123')
    profile = Profile.objects.create(user=user)
    assert str(profile) == 'testuser Profile'