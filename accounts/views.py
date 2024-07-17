# accounts/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.urls import reverse, NoReverseMatch

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to homepage after logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('accounts:user_login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')

        if 'profile_picture-clear' in request.POST:
            user.profile.profile_picture.delete()
        elif 'profile_picture' in request.FILES:
            user.profile.profile_picture = request.FILES['profile_picture']

        user.save()
        user.profile.save()

        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('accounts:user_profile')

    return render(request, 'accounts/profile.html')
