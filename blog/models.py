from django.db import models
from django.utils import timezone


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=20, default="no description")

    def __str__(self):
        return self.title


class Reaction(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=1)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.reaction} {self.amount}"
