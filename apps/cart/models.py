from django.db import models

from apps.product.models import Product, ProductAddOn, ProductAddOnOption
from apps.user.models import User
from apps.vendor.models import Vendor


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    addon_data = models.CharField(null=True, blank=True,max_length=25)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.addon_data


class CartItemAddOn(models.Model):
    cartitem = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    product_addon = models.ForeignKey(ProductAddOn, on_delete=models.CASCADE)


class CartItemAddOnOption(models.Model):
    cart_item_addon = models.ForeignKey(CartItemAddOn, on_delete=models.CASCADE,)
    Product_addon_option = models.ForeignKey(ProductAddOnOption, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2,  null=True)










