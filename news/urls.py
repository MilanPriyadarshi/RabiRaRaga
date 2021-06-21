from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.news,name="news"),
   path('<str:slug>',views.newsPost,name="newsPost"),
   # path('<str:slug>',views.blogPost,name="blogPost"),
   
]