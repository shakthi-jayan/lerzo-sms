from django.db import models

class Batch(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    assigned_to = models.ForeignKey("staffs.Staff",on_delete=models.PROTECT,related_name="batches")
    course = models.ForeignKey("courses.Course",on_delete=models.PROTECT,related_name="batches",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"

    class Meta:
        db_table = "batches"
        ordering = ["name"]
        verbose_name = "Batch"
        verbose_name_plural = "Batches"