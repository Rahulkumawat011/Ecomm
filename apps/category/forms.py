from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse

from apps.category.models import Category

# User = get_user_model()





class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','type']


