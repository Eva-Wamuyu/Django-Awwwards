from django.http import HttpResponse
from django.shortcuts import render,redirect
from django import views,urls
from requests import session
from ..models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,decorators
from ..forms import LoginForm,UserCreationForm
from django import forms
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET', 'POST'])
def logsin(request):
  user = request.user
  if user.is_authenticated:
    return HttpResponse(urls.reverse('home'))
    return redirect('home')
  
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
          login(request,user)
          return redirect('home')
      return render(request, 'authentication/login_form.html',{'form':form,'errors':'username or password is incorrect'})
    return render(request, 'authentication/login_form.html',{'form':form})
    
  return render(request, 'authentication/login_form.html',{'form':form})

    












class SignUp(APIView):
  def get(self,request):
    email = username = forms.CharField(max_length=255,widget=forms.EmailInput())
    form = UserCreationForm()
    return render(request,"authentication/form.html",{'form':form})
  
  def post(self,request):
    form = UserCreationForm(request.data)
    if form.is_valid():
      form.save()
      user = User.objects.get(username=form.cleaned_data['username'])
      profile = Profile.objects.create(user=user)
      Profile.save_profile(profile)
      print(profile)
      login(request,user)
      return redirect('logsin')
    errors = form.errors
    return render(request, 'authentication/form.html',{'form':form, 'errors':errors})



    
  