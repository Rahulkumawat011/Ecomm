from django.db import models

from apps import banner
from apps.category.models import Category
from apps.vendor.models import Vendor


# Create your models here.
class HomeBanner(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to='vendor_images/', blank=True, null=True)

    def __str__(self):
        return self.name
