from django.urls import path
from .views import StaffListAPI, StaffModifyAPI

urlpatterns = [
    path("",StaffListAPI.as_view(),name="staff_list_or_add"),
    path("<int:pk>/",StaffModifyAPI.as_view(),name="staff_modify")
]