from django.core.exceptions import ValidationError

CATEGORIES = "veg", "non-veg"
def validate_restaurant_name(restaurant_name):
    if restaurant_name == "create":
        raise ValidationError(f"{restaurant_name} cannot be used as a Restaurant Name.")

def validate_restarant_category(category):
    if category not in CATEGORIES:
        raise ValidationError(f"{category} is not a valid category in either of {CATEGORIES}")