from rest_framework import serializers
from .models import Profile, Garage, Voiture, Cle

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'

class CleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cle
        fields = '__all__'