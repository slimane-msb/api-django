from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .forms import UserForm

def home(request):
    return render(request, "home.html")


def cle(request):
    return render(request, "cle.html")

def garage(request):
    return render(request, "garage.html")

def voiture(request):
    return render(request, "voiture.html")


def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})
