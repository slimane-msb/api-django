from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .forms import UserForm,GarageForm
from api.models import Garage,Profile
from .forms import GarageSelectForm
import requests
from django.conf import settings



@login_required
def home(request):
    return render(request, "home.html")

@login_required
def profile(request):
    profile = request.user.profile
    return render(request, "profile.html",{'profile': profile})


def cle(request):
    return render(request, "cle.html")


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


def garage(request):
    garages = Garage.objects.all()
    return render(request, "garage.html",{'garages': garages})

def voiture_list(request):
    voitures = []
    form = GarageSelectForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        garage = form.cleaned_data['garage']
        url = request.build_absolute_uri(f'/api/voitures/{garage.id}/')
        response = requests.get(url)
        voitures = response.json()  
        
    return render(request, 'voiture.html', {'form': form, 'voitures': voitures})
