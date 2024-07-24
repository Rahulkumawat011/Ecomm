from django.conf import settings
from django.db import models
from apps.user.models import User

from apps import vendor


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    open_at = models.TimeField()
    close_at = models.TimeField()
    image = models.ImageField(upload_to='vendor_images/', blank=True, null=True)
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)

    def __str__(self):
        return self.name
