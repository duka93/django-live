from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("overview/", views.userinfo, name='userinfo'),
    path("usercreate/",views.CreateInfo.as_view(), name="createinfo"),
    path("overview/addweight/",views.AddCurrentWeight.as_view(), name="currentweight" ),
    path("overview/weightlist", views.ListCurrentWeight.as_view(), name="weightlist"),
    path("overview/history", views.history, name="history"),
    path("overview/<pk>/update", views.UpdateStartWeightAndHeight.as_view(), name="updateinfo"),
    path("overview/weightlist/<pk>/update", views.UpdateCurrentWeight.as_view(), name="update_weight"),
    path("overview/weightlist/<pk>/delete", views.DeleteCurrentWeight.as_view(),name="delete_weight"),
    path("instructions/",views.instructions_view, name="instructions")
]