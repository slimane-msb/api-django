from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .forms import GarageAddForm, GarageDeleteForm, GarageEditForm, UserForm,GarageForm
from api.models import Garage,Profile
from .forms import GarageSelectForm
import requests



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
    form_add = GarageAddForm(request.POST or None)
    form_edit = GarageEditForm(request.POST or None)
    form_delete = GarageDeleteForm(request.POST or None)

    if request.method == 'POST':
    
        if form_add.is_valid() and "form_add" in request.POST:
            data = {'nom': form_add.cleaned_data['name']}
            url = request.build_absolute_uri('/api/garages/add/')
            requests.post(url, json=data)
    
        elif form_edit.is_valid() and "form_edit" in request.POST:
            data = {'nom': form_edit.cleaned_data['name']}
            garage = form_edit.cleaned_data['garage']
            url = request.build_absolute_uri(f'/api/garages/{garage.id}/edit/')
            requests.put(url, json=data)

        elif form_delete.is_valid() and "form_delete" in request.POST:
            garage = form_delete.cleaned_data['garage']
            url = request.build_absolute_uri(f'/api/garages/{garage.id}/delete/')
            requests.delete(url)

    forms = {'form_add': form_add, 'form_edit': form_edit, 'form_delete': form_delete}
    return render(request, 'garage.html', forms)


def voiture_list(request):
    voitures = []
    form = GarageSelectForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        garage = form.cleaned_data['garage']
        url = request.build_absolute_uri(f'/api/voitures/{garage.id}/')
        response = requests.get(url)
        voitures = response.json()  
        
    return render(request, 'voiture.html', {'form': form, 'voitures': voitures})
