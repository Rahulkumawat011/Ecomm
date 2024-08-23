from django import forms

from apps.healthcare.models import Department, Category


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class CategorytForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class XlsUploadForm(forms.Form):
    xls_file = forms.FileField(label='Upload Xls File')