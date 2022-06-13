"""awwwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from account.views import api_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'profiles', api_views.ProfileView)
router.register(r'projects', api_views.ProjectView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('api/',include(router.urls)),
    path('api/auth-api-token/',obtain_auth_token),
   
]

handler404 = 'awwwards.views.page_not_found_view'