from django.urls import path
from .views import EnrollmentListAPI, EnrollmentModifyAPI

urlpatterns = [
    path("",EnrollmentListAPI.as_view(),name="enrollment_list_or_add"),
    path("<int:pk>/",EnrollmentModifyAPI.as_view(),name="enrollment_modify")
]