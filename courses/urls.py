from django.urls import path
from .views import CourseListAPI, CourseModifyAPI

urlpatterns = [
    path("",CourseListAPI.as_view(),name="course_list_or_add"),
    path("<int:pk>/",CourseModifyAPI.as_view(),name="course_modify")
]