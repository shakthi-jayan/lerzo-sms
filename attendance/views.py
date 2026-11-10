from rest_framework import generics
from .models import DailyAttendance, AttendanceRecord
from .serializers import DailyAttendanceSerializer, AttendanceRecordSerializer

class DailyAttendanceListAPI(generics.ListCreateAPIView):
    queryset = DailyAttendance.objects.all()
    serializer_class = DailyAttendanceSerializer

class DailyAttendanceModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyAttendance.objects.all()
    serializer_class = DailyAttendanceSerializer

class AttendanceRecordListAPI(generics.ListCreateAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

class AttendanceRecordModifyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer