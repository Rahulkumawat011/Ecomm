from django import forms

from apps.product.models import Product, ProductAddOn, ProductAddOnOption


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'product_name', 'price', 'description', 'available', 'stock', 'is_feature', 'is_popular']


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()


class CreateAddProductForm(forms.ModelForm):
    class Meta:
        model = ProductAddOn
        fields = ['title', 'type', 'is_required']


class CreateAddProductOptionForm(forms.ModelForm):
    class Meta:
        model = ProductAddOnOption
        fields = ['addon', 'title', 'price']

