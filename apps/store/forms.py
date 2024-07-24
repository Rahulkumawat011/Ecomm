from apps.store.models import Store
from django import forms


class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'open_at', 'close_at', 'description', 'country', 'pincode',  'landmark', 'city', 'state']