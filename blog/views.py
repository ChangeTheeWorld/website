from django.shortcuts import render, get_object_or_404

from .models import BlogPost, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(req):
    """
    the view for the url /blog, shows the list of blogposts
    """
    content = {"posts": BlogPost.objects.all()}
    return render(req, "blog/index.html", content)


def blog(req, blog_id):
    """
    the page for the blogpost
    """
    post = get_object_or_404(BlogPost, pk=blog_id)
    return render(req, "blog/blog.html", {"post": post})


def comment(req, blog_id):
    """
    where the form send the request when someone comments on a post
    """
    post = BlogPost.objects.get(id=blog_id)
    blog_comment = req.POST["comment"]
    author = req.POST["author"]
    post.comment_set.create(content=blog_comment, author=author)
    post.save()
    return HttpResponseRedirect(reverse('blog', args=[post.id]))
