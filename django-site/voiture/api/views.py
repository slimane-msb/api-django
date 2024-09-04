from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    my_dictionary = {"a": 1, "b": 2}
    return JsonResponse(my_dictionary)

