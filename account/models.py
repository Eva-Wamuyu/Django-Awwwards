from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Profile(models.Model):
  profile_pic = models.ImageField(upload_to = 'Awards', default="Awards/avatars_kuiof2.png")
  user_bio = models.CharField(max_length=255, blank=True)
  contact_information = models.URLField()
  projects = models.ManyToManyField('Project', blank=True, related_name="projects_posted")
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_profile(self):
    self.save()
  
  def del_profile(self):
    self.delete()

  def profile_projects(self,pk):
    return Project.objects.filter(profile=pk)
    


class Project(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  title = models.CharField(max_length=120)
  project_cover = models.ImageField(upload_to = 'Awards')
  description = models.TextField()
  url = models.URLField()
  votes = models.ManyToManyField('Vote',blank=True, related_name='votes')

  def save_project(self):
    self.save()

  def project_votes(self,pk):
    project=Project.objects.get(pk=pk)
    return Vote.objects.filter(project=project.id)

  @classmethod
  def search_project(cls,search):
    return cls.objects.filter(title__icontains=search).all()

  

class Vote(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  voter = models.ForeignKey(Profile,on_delete=models.CASCADE)
  design = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  usability = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
  content = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])

 
  
  