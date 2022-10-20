from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("overview/", views.userinfo, name='userinfo'),
    path("usercreate/",views.CreateInfo.as_view(), name="createinfo")
]