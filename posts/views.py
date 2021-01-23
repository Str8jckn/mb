from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.contrib import admin
from django.urls import path, include

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

context_object_name = 'all_posts_list'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')), # new
]


# Create your views here.
