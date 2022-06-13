from django.shortcuts import render,redirect,reverse
from requests import Response, session
from django.http import Http404, HttpResponseRedirect
from account.models import Project, Profile,Vote
from ..forms import AddProjectForm, RatingForm,UpdateProfile
from ..serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import logout,decorators
from django.contrib.auth.models import User
# Create your views here.

def handle_image(name,f):
    url = f"https://res.cloudinary.com/dbddkobs4/image/upload/v1/Awards/{name}"
    with open('url', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def home(request):
  form = AddProjectForm()
  projects = Project.objects.all()
  
  if request.method == 'POST':
    form = AddProjectForm(request.POST,request.FILES)
    if form.is_valid():
      
      #handle_image(form.cleaned_data['cover'],request.FILES['photo'])
      profile = Profile.objects.get(user=request.user)
      new_project = Project(profile=profile,title=form.cleaned_data['title'],description=form.cleaned_data['description'],url=form.cleaned_data['url'],project_cover=form.cleaned_data['cover'])
      new_project.save_project()
      form = AddProjectForm()
      return HttpResponseRedirect(reverse("home"))
    return render(request, 'account/index.html',{'form':form, 'projects':projects})
  return render(request, 'account/index.html',{'form':form,'projects':projects})
  


@decorators.login_required(login_url="/login")
def details(request,pk):
  
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    raise Http404
  votess = project.project_votes(project.id)
  if project.profile.user != request.user:
    form = RatingForm()
    if request.method == 'POST':
      form = RatingForm(request.POST)
      if form.is_valid():
        profile = Profile.objects.get(user=request.user)
        new_vote = Vote(project=project, voter=profile,design=form.cleaned_data['design'],usability=form.cleaned_data['usability'],content=form.cleaned_data['content'])
        new_vote.save()
        
        return HttpResponseRedirect(reverse("details", kwargs={'pk':project.id}))
      # serializer =ProjectSerializer(project,context=context)
      context={'request': request,'project': project,'form': form, 'votess':votess}
      return render(request,'account/details.html',context=context)
  else:
      form = None
  context={'request': request,'project': project,'message': "You can't rate your project", 'votess':votess,'form': form}
  return render(request,'account/details.html',context=context)
  
  # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@decorators.login_required(login_url="/login")
def profile(request,username):
  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    raise Http404
  user = User.objects.get(username=username)
  profile = Profile.objects.get(user=user)
  projects = profile.profile_projects(profile)
  
  return render(request, 'account/profile.html',{'projects':projects, 'profile':profile})

@decorators.login_required(login_url="/login")
def vote(request,pk):
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    raise Http404
  if project.profile == 1:
    message = "You cannot vote on your project"
    context={'request': request, 'message': message}
  else:
    form = RatingForm()
    context={'request': request, 'form': form}

  return render(request,'account/vote.html',context=context)

@decorators.login_required(login_url="/login")
def settings(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  form =  UpdateProfile(instance=profile)
  if request.method == 'POST':
    form =  UpdateProfile(files=request.FILES,data=request.POST)
    print(form.errors)
    if form.is_valid():
      profile.profile_pic = form.cleaned_data['profile_pic']
      profile.contact_information=form.cleaned_data['contact_information']
      profile.user_bio = form.cleaned_data['user_bio']
      profile.save()
      form = UpdateProfile(instance=profile)
      return HttpResponseRedirect(reverse("settings"))
    return render(request,'account/settings.html',{'form':form})
  return render(request,'account/settings.html',{'form':form})
  


def search(request):
  form = AddProjectForm()
  msg = 'No results found for term'
  projects = None
  if 'search' in request.GET and request.GET['search']:
    searchterm = request.GET['search']
    projects = Project.search_project(searchterm)

    form = AddProjectForm()
    return render(request,'account/index.html',{'form':form,'projects':projects})
  return render(request,'account/index.html',{'form':form,'projects':projects,'msg':msg})


@decorators.login_required(login_url="/login")
def members(request):
  profiles = Profile.objects.all()
  print(profiles)
  return render(request,'account/members.html',{'profiles':profiles})


def documentation(request):
  return render(request,'account/documentation.html')


@decorators.login_required(login_url="/login")
def losgout(request):
  logout(request)
  return HttpResponseRedirect("/")

  