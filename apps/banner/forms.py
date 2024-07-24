
from django import forms

from apps.banner.models import HomeBanner


class CreateBannerForm(forms.ModelForm):
    class Meta:
        model = HomeBanner
        fields = ['vendor', 'category', 'name', 'is_active', 'image']
