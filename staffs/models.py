from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="staffs/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "staffs"
        ordering = ["name"]
        verbose_name = "Staff"
        verbose_name_plural = "Staff"