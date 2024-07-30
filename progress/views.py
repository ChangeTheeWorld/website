from django.shortcuts import render
import requests

from changeTheWorld import settings


# Create your views here.


def index(request):
    repos = requests.get("https://api.github.com/orgs/changetheeworld/repos", headers={
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer " + settings.SECRET_TOKEN,
        "X-GitHub-Api-Version": "2022-11-28"
    })
    print(repos.json())
    return render(request, 'progress/index.html', context={'repos': repos.json()})
