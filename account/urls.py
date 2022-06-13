from django.urls import path
from .views import account,authentication,api_views




urlpatterns = [
  path("",account.home, name="home"),
  path("login",authentication.logsin, name="logsin"),
  path("signup",authentication.SignUp.as_view(), name="signup"),
  path("settings/",account.settings, name="settings"),
  path("user/<username>",account.profile, name="profile"),
  path('logout',account.losgout, name='logsout'),
  path('image/<pk>',account.details, name='details'),
  path('image/vote/<pk>',account.vote, name='vote'),
  path('search/', account.search, name='search'),
  path('members/', account.members, name='members'),
  path('documentation', account.documentation, name='documentation'),

  
   
]

