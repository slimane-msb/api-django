from django.contrib import admin

# Register your models here.
from .models import Voiture, Garage, Cle

admin.site.register(Voiture)   
admin.site.register(Garage)   
admin.site.register(Cle)   