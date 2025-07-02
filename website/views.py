from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages 

# Create your views here.



def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']    

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('home')
        
        else:
            messages.success(request, "Email or password isn't correct")
    return render(request, 'home.html', {})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})