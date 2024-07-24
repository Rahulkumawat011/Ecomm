from django import forms

from apps.vendor.models import Vendor


class CreateVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['user', 'name', 'address', 'open_at', 'close_at',  'image',  'lat', 'long',]