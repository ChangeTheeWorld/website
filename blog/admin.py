from django.contrib import admin
from .models import BlogPost, Reaction
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Reaction)
