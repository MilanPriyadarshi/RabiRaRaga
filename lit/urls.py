from django.urls import path
from . import views
urlpatterns = [
    path('', views.lit, name='lit'),
    path('<str:slug>',views.litPost,name="litPost"),

]