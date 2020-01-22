from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_restarant_category, validate_restaurant_name
from userauth.models import CustomUser

# Create your models here.
class RestaurantLocation(models.Model):
    # name = models.CharField(max_length = 120)
    # location = models.CharField(max_length=120,null=True,blank=True)
    name = models.CharField(max_length=120, validators=[validate_restaurant_name])
    location = models.CharField(max_length=120,null=True,blank=True)

    # category = models.CharField(max_length=120,null=True,blank=True)
    category = models.CharField(max_length=120, null=True, blank=True,validators=[validate_restarant_category])
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    # on_delete le kunai user delete garda purai tesko related restaurants delete huncha
    timestamp = models.DateTimeField(auto_now_add=True)#to add in current time auto add now
    updated = models.DateTimeField(auto_now=True)#it updates every time changes are made
    slug = models.SlugField(null=True,blank=True)

    def __str__(self): #str function chai restaurant ko list user lai dekhauna use garni
        return self.name

    # def __repr__(self): #repr or represent function chai logging ma use garni
    #     return f"__class__.__name__)"

def pre_save_receiver(sender, instance, *args, **kwargs):
    print("saving {}".format(instance))
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def post_save_receiver(sender, instance, created, *args, **kwargs):
    print("saved ()".format(created))

pre_save.connect(pre_save_receiver, sender=RestaurantLocation)

post_save.connect(post_save_receiver, sender=RestaurantLocation)
