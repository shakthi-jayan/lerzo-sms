from django.urls import path
from .views import StudentListAPI, StudentModifyAPI

urlpatterns = [
    path("",StudentListAPI.as_view(),name="student_list_or_add"),
    path("<int:pk>/",StudentModifyAPI.as_view(),name="student_modify")
]