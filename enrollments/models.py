from django.db import models

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    ]
    student = models.ForeignKey('students.Student', on_delete=models.PROTECT, related_name='enrollments')
    batch = models.ForeignKey("batches.Batch", on_delete=models.PROTECT, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'batch')

    def __str__(self):
        return f"{self.student.first_name} enrolled in {self.batch.name}"