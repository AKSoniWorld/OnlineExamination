from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from .models import (
    Profile
)

from .forms import (
    LoginForm,
    ProfileForm,
    ProfileAddForm
)



# Create your views here.

class LoginView(views.View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'login.html',
            context={
                'form' : LoginForm()
            }
        )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('profiles:profile')
            else:
                form.add_error("username", "Invalid Details")
                return render(
                    request,
                    'login.html',
                    context={
                        'form' : form,
                        "errors" : "Worng Password",
                    }
                )
        else:
            return render(
                request,
                'login.html',
                context={
                    'form' : form
                }
            )

def LogoutView(request):
    logout(request)
    return redirect("profiles:login")

class RegisterView(views.View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'register.html',
            context={
                'form' : ProfileAddForm()
            }
        )

    def post(self, request, *args, **kwargs):
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            Profile.objects.create(
                user = user
            )
            login(request, user)
            return redirect('profiles:profile')
        else: 
            return render(
                request,
                'register.html',
                context={
                    'form' : form
                }
            )

class ProfileView(LoginRequiredMixin, views.View):

    login_url = "/profile/login/"
    
    def get(self, request, cid = None, *args, **kwargs):
        if not cid:
            return render(
                request,
                'profile.html',
                context={
                    'form' : ProfileForm(
                        instance=request.user.profile
                    )
                }
            )
        else: 
            try:
                return render(
                    request,
                    'profile.html',
                    context={
                        'form' : ProfileForm(
                            instance=Profile.objects.get( id = cid )
                        )
                    }
                )
            except Exception as e:
                return HttpResponse(
                    status = 404
                )

    def post(self, request, cid = None, *args, **kwargs):
        if cid:
            try:
                profile = Profile.objects.get(id = cid)
            except Exception as e :
                return HttpResponse(
                    status = 404
                )
        else:
            profile = request.user.profile
        
        form = ProfileForm(
            instance=profile,
            data=request.POST,
        )
        if form.is_valid():
            form.save()
            return render(
                request,
                'profile.html',
                context={
                    'form' : form,
                    "errors" : "Profile Updated Sucessfully",
                }
            )
        else:
            return render(
                request,
                'profile.html',
                context={
                    'form' : form,
                }
            )

class AdminProfileListView(views.View):
    
    def get(self, request, *args, **kwargs):
        pass