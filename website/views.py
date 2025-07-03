from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import SignUpForm, AddRecordForm
from django.contrib.auth.models import User
from .models import Record
# Create your views here.



def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('home')
        
        else:
            messages.success(request, "Email or password isn't correct")
            
    context = {'records': records}
    return render(request, 'home.html', context)


@login_required(login_url='home')
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
            if request.user.is_authenticated:
                return redirect('home')
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})


@login_required(login_url='home')
def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        context = {'record': record}
        return render(request, 'record.html', context)
    else:
        messages.success(request, 'You must be logged in to view that page')
        return redirect('home')
    
    
@login_required(login_url='home')
def delete_record(request, pk):
    if request.user.is_authenticated:
        deleted = Record.objects.get(id=pk)
        deleted.delete()
        messages.success(request, 'Record Deleted Successfully!')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to view that page')
        return redirect('home')
    
    
@login_required(login_url='home')
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Added Successfully!')
                return redirect('home')
        return render(request, 'add_record.html', {'form': AddRecordForm})
    else:
        messages.success(request, 'You must be logged in to view that page')
        return redirect('home')
    
    
    
@login_required(login_url='home')
def edit_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Updated Successfully!')
                return redirect(f'home')
        else:
            return render(request, 'edit_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to view that page')
        return redirect('home')