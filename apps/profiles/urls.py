from django.urls import path, include

from .views import (
    LoginView,
    LogoutView,
    RegisterView,
    ProfileView,
    AdminProfileListView,
)

urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(), 
        name = "login"
    ),
    path(
        'logout/', 
        LogoutView, 
        name = "logout"
    ),
    path(
        'register/',
        RegisterView.as_view(),
        name = "register",
    ),
    path(
        'profile/',
        ProfileView.as_view(),
        name = "profile",
    ),
    path(
        'admin/profile/<int:cid>/details/',
        ProfileView.as_view(),
        name = "profile",
    ),
    path(
        'admin/profile/list/',
        AdminProfileListView.as_view(),
        name = "profileadminlist",
    ),
]