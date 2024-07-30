import requests
import json
from django.shortcuts import render

from changeTheWorld import settings


# Create your views here.


def home(request):
    members = requests.get("https://api.github.com/orgs/changetheeworld/members", headers={
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer " + settings.GH_TOKEN,
        "X-GitHub-Api-Version": "2022-11-28"
    })

    return render(request, 'index.html', {'members': members.json()})
