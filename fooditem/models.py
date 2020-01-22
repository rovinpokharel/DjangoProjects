from django.db import models
from userauth.models import CustomUser
from restaurants.models import RestaurantLocation

# Create your models here.
class FoodItem(models.Model):
    #associations
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation,on_delete=models.CASCADE)

    #FoodItems data
    name = models.CharField(max_length=100)
    contents = models.TextField(help_text='seperate by comma')
    excludes = models.TextField(help_text='seperate by comma',blank=True,null=True)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{__class__.__name__}({self.name} <{self.user!r}> <{self.restaurant!r}>)"

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")
