# accounts/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

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

#@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to profile view after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)