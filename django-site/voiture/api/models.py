from django.db import models
from django.contrib.auth import get_user_model

class Garage(models.Model):
    nom = models.CharField(max_length=30, blank=False, null=False)
    

class Voiture(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    couleur = models.CharField(max_length=30, blank=False, null=False)
    immatriculation = models.CharField(max_length=9, blank=False, null=False)
    marque = models.CharField(max_length=30, blank=False, null=False)
    modele = models.CharField(max_length=30, blank=False, null=False)


class Cle(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    etat_pret = models.BooleanField(blank=False, null=False)
    date_pret = models.DateField(blank=False, null=False)
    date_rendu = models.DateField(blank=False, null=False)



