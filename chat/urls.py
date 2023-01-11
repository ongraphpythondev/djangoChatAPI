from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('chat/', views.Home.as_view(),name="chat"),
    path('signup/',views.Signup.as_view(),name="signup"),
    path('login/',views.LoginView.as_view(),name="login")
]