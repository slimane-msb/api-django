from django import forms
from django.contrib.auth import get_user_model


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



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={
            'placeholder': 'usss'
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
