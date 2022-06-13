from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


#  @classmethod
#     def setUpTestData(cls):

class TestProfile(TestCase):
  def setUp(self):
    user = User.objects.create(
      username="Wamu",
      password="12345"
    )
    new_prof = Profile.objects.create(
      profile_pic = "default.png",
       user_bio = "user got no bio",
       user = user
    )
   
  def test_init(self):
    user = User.objects.get(username = "Wamu")
    new_prof = Profile.objects.get(user=user)
    self.assertIsInstance(new_prof,Profile)


  def test_save(self):
    new_prof = Profile.objects.get(pk=1)
    new_prof.save_profile()
    self.assertEquals(len(Profile.objects.all()),1)
  

  def test_delete_profile(self):
    profile = Profile.objects.get(pk=1)
    profile.del_profile()
    self.assertEquals(len(Profile.objects.all()),0)
  
  def test_multi_save(self):
    user = User.objects.create(
      username="Wamu2",
      password="12345"
    )
    new_prof = Profile.objects.create(
      profile_pic = "default.png",
       user_bio = "user2 got no bio",
       user = user
    )
    new_prof = Profile.objects.get(pk=1)
    new_prof.save_profile()
    self.assertEquals(len(Profile.objects.all()),2)



  



class TestProject(TestCase):
  def setUp(self):
    user = User.objects.create(
      username="Wamu",
      password="12345"
    )
    profile = Profile(user=user)
    profile.save()
    new_proj = Project(
      profile = profile,
      title = "Project Title",
      description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum pulvinar hendrerit turpis, ut tempor elit cursus nec. Maecenas vel commodo sapien. Vestibulum sit amet fringilla diam. Nullam facilisis interdum urna, vitae imperdiet risus aliquam a. Proin imperdiet feugiat tellus, ac posuere orci tempus sed. Fusce et erat eget velit rhoncus commodo non id dui. Proin scelerisque enim sit amet nulla consectetur, id euis",
      project_cover = "cover.png",
    )
    new_proj.save()
    

  def test_init(self):
    new_proj = Project.objects.get(pk=1)
    self.assertIsInstance(new_proj,Project)


  def test_save(self):
    new_proj = Project.objects.get(pk=1)
    new_proj.save_project()
    self.assertEquals(len(Project.objects.all()),1)









class TestVote(TestCase):
  def setUp(self):
    user = User(username="Wamu")
    user.save()
    voter = Profile(user=user)
    voter.save()
    proj = Project(title="Test",profile=voter)
    proj.save()
    
    vote = Vote.objects.create(
      project=proj,
      voter=voter,
      design = 10,
      usability = 12,
      content = 7,

    )

  def test_int(self):
    new_vote = Vote.objects.get(pk=1)
    self.assertIsInstance(new_vote,Vote)

    





