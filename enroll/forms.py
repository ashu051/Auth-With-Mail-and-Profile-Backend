from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Mail


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name','last_name','email','username']
class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class MessageForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields=['message','email']