from django.db import models
from django.utils import timezone

class Student(models.Model):
    enrollment_number = models.CharField(max_length=15,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True,blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    fees = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    balance_fees = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    joining_date = models.DateField(default=timezone.localdate)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey("courses.Course",on_delete=models.PROTECT,related_name="students",null=True,blank=True)
    staff = models.ForeignKey("staffs.Staff",on_delete=models.PROTECT,related_name="students",null=True,blank=True)
    batch = models.ForeignKey("batches.Batch",on_delete=models.PROTECT,related_name="students",null=True,blank=True)
    profile_image = models.ImageField(upload_to='students/',null=True,blank=True)

    def __str__(self):
        return f"{self.enrollment_number} - {self.name}"

    class Meta:
        db_table = "students"
        ordering = ["-created_at"]
        verbose_name = "Student"
        verbose_name_plural = "Students"
