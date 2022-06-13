from .models import Profile, Project,Vote
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Vote)
admin.site.register(Project)