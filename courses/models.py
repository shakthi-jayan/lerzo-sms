from django.db import models
class Course(models.Model):

    name = models.CharField(max_length=100,unique=True)
    duration_months = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "courses"
        ordering = ["name"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"
