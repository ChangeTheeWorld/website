from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.blog, name='blog'),
    path('<int:blog_id>/comment', views.comment, name='comment'),
    path('commentlike/<int:comment_id>', views.comment_like, name='comment_like'),
]