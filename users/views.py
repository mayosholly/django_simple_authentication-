from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms 

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')  # Redirect to the home page or another appropriate page
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})