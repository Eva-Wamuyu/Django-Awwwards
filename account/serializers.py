from rest_framework import serializers
from .models import Profile,Project


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Profile
    exclude = ['user']



class ProjectSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Project
    fields = '__all__'