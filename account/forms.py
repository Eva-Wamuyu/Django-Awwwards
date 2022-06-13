from django.forms import CharField,Form, ImageField, ModelForm,PasswordInput,Form, TextInput, Textarea, URLField, IntegerField
from django.contrib.auth import models, forms

from account.models import Vote,Profile

class LoginForm(Form):
  username = CharField(max_length=255)
  password = CharField(max_length=255,widget=PasswordInput)


class UserCreationForm(forms.UserCreationForm):
  class Meta:
    model = models.User
    fields = [
    'username',
    'email',
    'password1',
    'password2'
    ]



class AddProjectForm(Form):
  title = CharField(max_length=255, required=True)
  description = CharField(widget=Textarea)
  url = URLField(max_length=255, required=True)
  cover = ImageField()

class RatingForm(Form):
  design = IntegerField(min_value=1, max_value=10)
  content = IntegerField(min_value=1, max_value=10)
  usability = IntegerField(min_value=1, max_value=10)
  

class UpdateProfile(ModelForm):
  class Meta:
    model = Profile
    exclude = ["projects", "user"]
    
    label = {
      'contact_information': 'Github Link'
    }