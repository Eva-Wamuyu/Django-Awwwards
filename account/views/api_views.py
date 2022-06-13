from rest_framework import viewsets
from rest_framework import permissions
from ..models import Profile,Project
from ..serializers import ProfileSerializer,ProjectSerializer


class ProfileView(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [permissions.IsAuthenticated]


class ProjectView(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]