from django.db import models
from decimal import Decimal

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('UPI', 'UPI'),
        ('CARD', 'Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
    ]

    enrollment = models.ForeignKey(
        'enrollments.Enrollment', 
        on_delete=models.PROTECT, 
        related_name='payments'
    )

    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    receipt_number = models.CharField(max_length=50, unique=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='UPI')
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'payments'
        ordering = ['-payment_date']

    def __str__(self):
        return f"Receipt #{self.receipt_number} - {self.amount_paid} ({self.enrollment.student.first_name})"