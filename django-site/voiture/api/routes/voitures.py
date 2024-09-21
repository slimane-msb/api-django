from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import VoitureSerializer

from api.models import Profile, Garage, Voiture, Cle



@api_view(['GET'])
def get_voitures(request):
    voitures = Voiture.objects.all()
    serializer = VoitureSerializer(voitures, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_voiture(request, garageId):
    voiture = Voiture.objects.filter(garage=garageId)
    if not voiture:
        return Response({"detail": "Not found."}, status=404)
    serializer = VoitureSerializer(voiture,many=True)
    return Response(serializer.data)
