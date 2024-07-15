from django.views import generic
from .models import BlogPost
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogPostSerializer


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """fetches all posts"""
        return BlogPost.objects.order_by('-date_posted')


class BlogView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'post'


@api_view(['GET'])
def blog_endpoint(req, blog_id=None):
    print(blog_id)
    if blog_id is None:
        blogpost = BlogPost.objects.order_by('-pk')[0]
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)

    blogpost = BlogPost.objects.get(pk=blog_id)
    serializer = BlogPostSerializer(blogpost)
    return Response(serializer.data)


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
