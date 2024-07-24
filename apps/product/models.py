from django.db import models

from application.custom_models import DateTimeModel
from apps import product
from apps.category.models import Category
from apps.product.constants import PRODUCT_ADD_ON_TYPE
from apps.user.models import User
from apps.vendor.models import Vendor


# Create your models here.

class Product(DateTimeModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=20)
    product_name = models.CharField(max_length=20)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    available = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(default=False, null=True)
    is_popular = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.product_name


class ProductAddOn(DateTimeModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=20)
    title = models.CharField(max_length=50,)
    type = models.CharField(choices=PRODUCT_ADD_ON_TYPE, max_length=50, null=True, blank=True)
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProductAddOnOption(DateTimeModel):
    addon = models.ForeignKey(ProductAddOn, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,  null=True)

    def __str__(self):
        return self.title


class FavoriteProduct(DateTimeModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)







