from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        # email se user find karo
        from django.contrib.auth.models import User
        try:
            user_obj = User.objects.get(email=email)
            user = AuthenticationForm(request, username=user_obj.username, password=password)
        except:
            user = None

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

