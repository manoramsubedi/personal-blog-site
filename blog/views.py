from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *


# Create your views here.

# def index(request):
#     latest_post = Post.objects.all().order_by("-date")[:3] #last posted
#     context = {'posts': latest_post}
#     return render(request, 'blog/index.html', context)    

class index(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset() #fetch all data
        data = queryset[:3]       
        return data
    

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")[:3]
#     context = {'all_posts':all_posts}
#     return render(request, "blog/all-posts.html", context)

class posts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug) #left slug -> attribute from model | right slug -> argument
#     post_tags = identified_post.tags.all()
#     context = {'post': identified_post, "post_tags": post_tags}
#     return render(request, "blog/post-detail.html", context)

class post_detail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
    