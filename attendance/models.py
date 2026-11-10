from django.db import models

class DailyAttendance(models.Model):
    batch = models.ForeignKey("batches.Batch", on_delete=models.PROTECT, related_name="attendance_sessions")
    date = models.DateField()
    recorded_by = models.ForeignKey("staffs.Staff", on_delete=models.PROTECT, related_name="recorded_attendances")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "daily_attendance"
        unique_together = ('batch', 'date') 

    def __str__(self):
        return f"{self.batch.name} - {self.date}"

class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
    ]

    attendance_session = models.ForeignKey(DailyAttendance, on_delete=models.CASCADE, related_name="records")
    student = models.ForeignKey("students.Student", on_delete=models.PROTECT, related_name="attendance_records")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PRESENT')
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "attendance_records"
        unique_together = ('attendance_session', 'student') 

    def __str__(self):
        return f"{self.student.first_name} - {self.status} on {self.attendance_session.date}"