from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    # path('photo', views.photo, name='photo'),
    # path('country', views.country, name='country'),
    # path('state', views.state, name='state'),
    # path('lit', views.lit, name='lit'),

]