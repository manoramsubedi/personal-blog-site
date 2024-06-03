from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3] #last posted
    context = {'posts': latest_post}
    return render(request, 'blog/index.html', context)    

def posts(request):
    all_posts = Post.objects.all().order_by("-date")[:3]
    context = {'all_posts':all_posts}
    return render(request, "blog/all-posts.html", context)

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug) #left slug -> attribute from model | right slug -> argument
    post_tags = identified_post.tags.all()
    context = {'post': identified_post, "post_tags": post_tags}
    return render(request, "blog/post-detail.html", context)