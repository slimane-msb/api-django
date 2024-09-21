from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.views import LoginView

from api.models import Garage

class UserForm(forms.ModelForm):
    username = forms.CharField(
        max_length = 200, 
        label="", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username'
        })    
    )
    email = forms.CharField(
        max_length = 200, 
        label="", 
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email'
        })    
    )
    password = forms.CharField(
        max_length = 200, 
        label="", 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password'
        })    
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']



class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label = "",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label = "",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'placeholder': 'Password'
        }),
    )


class MyLoginView(LoginView):
    form_class = MyAuthenticationForm



class GarageForm(forms.ModelForm):
    pass



class VoitureSelectForm(forms.Form):
    garage = forms.ModelChoiceField(
        queryset = Garage.objects.all(), 
        empty_label = "Select a Garage"
    )

class VoitureAddForm(forms.Form):
    garage = forms.ModelChoiceField(
        queryset = Garage.objects.all(), 
        empty_label = "Select a Garage"
    )

    couleur = forms.CharField(
        max_length = 200, 
        label="", 
        widget = forms.TextInput(attrs={
            'placeholder': 'Entrer le nom'
        })    
    )

    immatriculation = forms.CharField(
        max_length = 200, 
        label="", 
        widget = forms.TextInput(attrs={
            'placeholder': 'Entrer le nom'
        })    
    )

    marque = forms.CharField(
        max_length = 200, 
        label="", 
        widget = forms.TextInput(attrs={
            'placeholder': 'Entrer le nom'
        })    
    )

    modele = forms.CharField(
        max_length = 200, 
        label="", 
        widget = forms.TextInput(attrs={
            'placeholder': 'Entrer le nom'
        })    
    )

class GarageAddForm(forms.Form):
    name = forms.CharField(
        max_length = 200, 
        label="", 
        widget = forms.TextInput(attrs={
            'placeholder': 'Entrer le nom'
        })    
    )


class GarageEditForm(forms.Form):
    garage = forms.ModelChoiceField(
        queryset = Garage.objects.all(), 
        empty_label = "Select a Garage"
    )

    name = forms.CharField(
        max_length = 200, 
        label="", 
        widget = forms.TextInput(attrs={
            'placeholder': 'Entrer le nom'
        })    
    )

class GarageDeleteForm(forms.Form):
    garage = forms.ModelChoiceField(
        queryset = Garage.objects.all(), 
        empty_label = "Select a Garage"
    )