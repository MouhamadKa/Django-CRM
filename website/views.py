from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.



def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username=username, password=password)
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
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})