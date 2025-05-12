from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def menu(request):
    return render(request, "menu.html")

@login_required
def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "registration/login.html")

def close(request):
    logout(request)
    return redirect('login')