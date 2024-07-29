from django.urls import path
from .views import index

app_name = 'progress'
urlpatterns = [
    path('', index, name='index'),
]
