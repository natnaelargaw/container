from django.contrib import admin
from django.urls import path
from . import views
from .views import SignUpView
urlpatterns = [
    # path('', views.),
    path('profile/', views.user_profile, name="userprofile"),
    path("signup/", SignUpView.as_view(), name="signup"),

]
