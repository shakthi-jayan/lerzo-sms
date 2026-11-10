from django.urls import path
from .views import DailyAttendanceListAPI, DailyAttendanceModifyAPI,AttendanceRecordListAPI, AttendanceRecordModifyAPI

urlpatterns = [
    path('sessions/', DailyAttendanceListAPI.as_view(), name='attendance_session_list_add'),
    path('sessions/<int:pk>/', DailyAttendanceModifyAPI.as_view(), name='attendance_session_modify'),
    path('records/', AttendanceRecordListAPI.as_view(), name='attendance_record_list_add'),
    path('records/<int:pk>/', AttendanceRecordModifyAPI.as_view(), name='attendance_record_modify'),
]