from django import forms
from .models import ShippingAddress


class ShippingModelForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        exclude = ['user']


