from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    context = {"members_names":[]}
    return render(request, 'index.html')