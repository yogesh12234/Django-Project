from django.shortcuts import render
from django.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

def login(request):
    pass

def dashborad(request):
    pass

def logout(request):
    pass