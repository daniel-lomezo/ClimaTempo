from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Table_Id_City
import requests, json
from django.contrib import messages
from django.core import serializers




def api_get_city_names_filter_data(request, country):
   data = Table_Id_City.objects.filter(country=country)
   qs_json = serializers.serialize('json', data)
   return JsonResponse(qs_json, safe=False)


def api_get_city_names(request):
   data = Table_Id_City.objects.all()
   qs_json = serializers.serialize('json', data)
   return JsonResponse(qs_json, safe=False)




# Create your views here.

def index_view(request):
	return render(request, 'index.html')








