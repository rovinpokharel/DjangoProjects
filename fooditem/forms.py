from django import forms
from .models import FoodItem
from restaurants.models import RestaurantLocation

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = [
            "name",
            "restaurant",
            "contents",
            "excludes",
            "public"
        ]

    def __init__(self,user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        print(kwargs)
        self.fields["restaurant"].queryset = RestaurantLocation.objects.filter(owner=self.user)