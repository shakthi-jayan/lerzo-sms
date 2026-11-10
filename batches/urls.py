from django.urls import path
from .views import BatchListAPI, BatchModifyAPI

urlpatterns = [
    path("",BatchListAPI.as_view(),name="course_list_or_add"),
    path("<int:pk>/",BatchModifyAPI.as_view(),name="course_modify")
]