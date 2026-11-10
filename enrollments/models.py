from django.db import models
from django.db.models import Sum
from decimal import Decimal

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
        return f"{self.student.name} enrolled in {self.batch.name}"

@property
def total_paid(self):
    aggregate_result = self.payments.aggregate(total=Sum('amount_paid'))['total']
    return aggregate_result or 0.00

@property
def course_fee(self):
    if self.batch and self.batch.course and self.batch.course.fee_amount:
        return self.batch.course.fee_amount
    return 0.00

@property
def pending_balance(self):
    return max(Decimal('0.00'), self.course_fee - Decimal(str(self.total_paid)))