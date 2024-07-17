from django.urls import path

from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.BlogView.as_view(), name='blog'),
    path('<int:blog_id>/comment', views.comment, name='comment'),
    path('api/<int:blog_id>', views.blog_endpoint, name='blog-endpoint-specific'),
    path('api/', views.blog_endpoint, name='blog-endpoint'),
]