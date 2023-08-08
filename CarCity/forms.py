from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['brand', 'model', 'year', 'price', 'contact_info']

class FilterForm(forms.Form):
    brand = forms.CharField(max_length=100, required=False)
    model = forms.CharField(max_length=100, required=False)
    year = forms.IntegerField(required=False)
    price_min = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    price_max = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
