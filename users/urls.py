from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls"),name="login"),
    path("/signup",views.Signup.as_view(),name="signup")
]