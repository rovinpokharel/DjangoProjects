from django import forms
from .models import RestaurantLocation

class RestaurantLocationModelForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            "name",
            "location",
            "category",
        ]