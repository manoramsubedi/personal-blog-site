from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
#from django.views.generic.detail import DetailView
from django.views import View
from .models import *
from .forms import CommentForm


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

# class post_detail(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context

class post_detail(View):    

    def is_stored_post(self, request, post_id):
        #checkinf if post is added in session or not
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None: #if we have srored post
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)


        context = {
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form": CommentForm(),
            "comments":  post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)

        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST) #submitted form/data
        post = Post.objects.get(slug=slug) #fetch data for the given slug

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
                
        context = {
        "post":post,
        "post_tags":post.tags.all(),
        "comment_form": comment_form #same user submitted data
        }
        return render(request, "blog/post-detail.html", context)
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
          request.session["stored_posts"] = stored_posts
        
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")
    