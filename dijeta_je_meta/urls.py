from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("overview/", views.UserInfo.as_view(), name='userinfo')
]