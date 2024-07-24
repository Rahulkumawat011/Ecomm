from django.db import models
from application.custom_models import DateTimeModel


class Store(DateTimeModel):
    name = models.CharField(max_length=20)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    description = models.TextField(max_length=100)
    country = models.CharField(max_length=20, null=True)
    pincode = models.CharField(max_length=6, null=True)
    landmark = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

