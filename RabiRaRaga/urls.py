"""RabiRaRaga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('', include('home.urls')),
    path('photo/', include('photo.urls')),
    path('lit/', include('lit.urls')),
]

# manually added for admin panel

admin.site.site_header = 'RabiRaRaga Admin Panel'                    # default: "Django Administration"
admin.site.index_title = 'Admin'                 # default: "Site administration"
admin.site.site_title = 'Welcome to the admin panel of RabiRaRaga' # default: "Django site admin"
