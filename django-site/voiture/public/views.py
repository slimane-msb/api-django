from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .forms import GarageAddForm, GarageDeleteForm, GarageEditForm, UserForm,GarageForm, VoitureAddForm, VoitureSelectForm
from api.models import Garage,Profile
import requests
from django.contrib import messages




@login_required
def home(request):
    return render(request, "home.html")

@login_required
def profile(request):
    profile = request.user.profile
    return render(request, "profile.html",{'profile': profile})

@login_required
def cle(request):
    return render(request, "cle.html")


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def garage(request):
    form_add = GarageAddForm()
    form_edit = GarageEditForm()
    form_delete = GarageDeleteForm()

    if request.method == 'POST':
    
        if "form_add" in request.POST:
            form_add = GarageAddForm(request.POST or None)
            if form_add.is_valid() :
                data = {'nom': form_add.cleaned_data['name']}
                url = request.build_absolute_uri('/api/garages/add/')
                requests.post(url, json=data)
                messages.success(request, "form_add submitted successfully!", extra_tags="form_add")
    
        elif  "form_edit" in request.POST:
            form_edit = GarageEditForm(request.POST or None)
            if form_edit.is_valid():
                data = {'nom': form_edit.cleaned_data['name']}
                garage = form_edit.cleaned_data['garage']
                url = request.build_absolute_uri(f'/api/garages/{garage.id}/edit/')
                requests.put(url, json=data)
                messages.success(request, "form_edit submitted successfully!", extra_tags="form_edit")

        elif "form_delete" in request.POST:
            form_delete = GarageDeleteForm(request.POST or None)
            if form_delete.is_valid() :
                garage = form_delete.cleaned_data['garage']
                url = request.build_absolute_uri(f'/api/garages/{garage.id}/delete/')
                requests.delete(url)
                messages.success(request, "form_delete submitted successfully!",extra_tags="form_delete")

    forms = {
        'form_add': form_add, 
        'form_edit': form_edit, 
        'form_delete': form_delete,
    }
    return render(request, 'garage.html', forms)

@login_required
def voiture(request):
    voitures = []
    
    form_select = VoitureSelectForm()
    form_add = VoitureAddForm()

    if request.method == 'POST':
    
        if "form_select" in request.POST:
            form_select = VoitureSelectForm(request.POST or None)
            if form_select.is_valid() :
                garage = form_select.cleaned_data['garage']
                url = request.build_absolute_uri(f'/api/voitures/{garage.id}/')
                response = requests.get(url)
                voitures = response.json() 
                if response.status_code != 200 : 
                    messages.error(request, "aucune voiture dans ce garage!", extra_tags="form_select")

        elif  "form_add" in request.POST:
            form_add = VoitureAddForm(request.POST or None)
            if form_add.is_valid() :
                data = form_add.cleaned_data
                data["garage"] = data["garage"].id
                url = request.build_absolute_uri(f'/api/voitures/add/')
                response = requests.post(url, json=data)
                messages.success(request, "form_add submitted successfully!", extra_tags="form_add")

    forms = {'form_select': form_select, 'form_add' : form_add ,'voitures': voitures}
    return render(request, 'voiture.html',forms )

