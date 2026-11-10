from rest_framework import serializers
from .models import DailyAttendance, AttendanceRecord

class AttendanceRecordSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.first_name', read_only=True)

    class Meta:
        model = AttendanceRecord
        fields = ['id', 'attendance_session', 'student', 'student_name', 'status', 'remarks']

class DailyAttendanceSerializer(serializers.ModelSerializer):
    # The 'records' variable matches the related_name defined in the AttendanceRecord model
    records = AttendanceRecordSerializer(many=True, read_only=True)
    batch_name = serializers.CharField(source='batch.name', read_only=True)

    class Meta:
        model = DailyAttendance
        fields = ['id', 'batch', 'batch_name', 'date', 'recorded_by', 'created_at', 'records']