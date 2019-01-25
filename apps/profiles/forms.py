from django import forms
from django.contrib.auth.models import User

from .models import (
    Profile
)

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label = "User Name : "
    )
    password = forms.CharField(
        max_length=50,
        label = "Password : ",
        widget = forms.PasswordInput(),
    )

    def clean_username(self, *args, **kwargs):
        try:
            User.objects.get( username = self.cleaned_data['username'] )
            return self.cleaned_data['username']
        except Exception as e:
            raise forms.ValidationError("No User Found, please go to register and create one") 

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = []

class ProfileAddForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label = "User Name : "
    )
    password1 = forms.CharField(
        max_length=50,
        label = "Password : ",
        widget = forms.PasswordInput(),
    )
    password2 = forms.CharField(
        max_length=50,
        label = "Confirm Password : ",
        widget = forms.PasswordInput(),
    )

    def clean_username(self, *args, **kwargs):
        try:
            User.objects.get( username = self.cleaned_data['username'] )
            raise forms.ValidationError("User Already Exist") 
        except forms.ValidationError as e :
            raise forms.ValidationError("User Already Exist") 
        except Exception as e:
            return self.cleaned_data['username']

    def clean_password1(self, *args, **kwargs):
        if self.data['password1'] == "" or self.data['password2'] == "":
            raise forms.ValidationError("Password Can not be blank")
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError("Password Does not Match")
        else:
            return self.cleaned_data['password1']
           
