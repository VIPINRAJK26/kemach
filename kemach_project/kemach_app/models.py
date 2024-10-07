from django.db import models
from django.contrib.auth.models import User

class Machinery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    available_for_test_drive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class TestDrive(models.Model):
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    test_drive_date = models.DateTimeField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.machinery.name} on {self.test_drive_date}"

