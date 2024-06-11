from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index.as_view(), name='index'),
   path('posts', views.posts.as_view(), name='posts'),
   path('posts/<slug:slug>', views.post_detail.as_view(), name='post-detail-page')
    
]