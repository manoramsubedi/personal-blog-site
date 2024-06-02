from django.shortcuts import render

from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountain",
        "image": "mountains.jpg",
        "author": "Manoram",
        "date": date(2024, 5, 28),
        "title": "Mountain Hiking",
        "excerpt": "here's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit voluptates, at dolorem velit accusamus asperiores ex architecto hic libero rem a, doloribus pariatur natus. Facere quibusdam eos mollitia dolorem perspiciatis."
    },

    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Manoram",
        "date": date(2024, 2, 28),
        "title": "Programming is great!",
        "excerpt": "here's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit voluptates, at dolorem velit accusamus asperiores ex architecto hic libero rem a, doloribus pariatur natus. Facere quibusdam eos mollitia dolorem perspiciatis."
    },

    {
        "slug": "woods",
        "image": "woods.jpg",
        "author": "Manoram",
        "date": date(2024, 3, 28),
        "title": "Nature is the best!",
        "excerpt": "here's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit voluptates, at dolorem velit accusamus asperiores ex architecto hic libero rem a, doloribus pariatur natus. Facere quibusdam eos mollitia dolorem perspiciatis."
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:] 
    context = {'posts': latest_post}
    return render(request, 'blog/index.html', context)    

def posts(request):
    context = {'all_posts':all_posts}
    return render(request, "blog/all-posts.html", context)

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    context = {'post': identified_post}
    return render(request, "blog/post-detail.html", context)