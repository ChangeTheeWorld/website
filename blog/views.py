from django.shortcuts import render, get_object_or_404

from .models import BlogPost, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(req):
    content = {"posts": BlogPost.objects.all()}
    return render(req, "blog/index.html", content)


def blog(req, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    return render(req, "blog/blog.html", {"post": post})


def comment(req, blog_id):
    post = BlogPost.objects.get(id=blog_id)
    blog_comment = req.POST["comment"]
    post.comment_set.create(content=blog_comment)
    post.save()
    return HttpResponseRedirect(reverse('blog', args=[post.id]))


def comment_like(req, comment_id):
    comm = Comment.objects.get(id=comment_id)
    post = comm.blog_post
    print(req.POST)
    val = 0
    if "like" in req.POST:
        print(req.POST["like"])
        val = int(req.POST["like"])

    comm.likes += val
    comm.save()
    return HttpResponseRedirect(reverse('blog', args=[post.id]))
