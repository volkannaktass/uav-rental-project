from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from user.models import UserProfile
from .utils import user_listing_path
from .const import BRANDS, MODELS, CATEGORY



### Created models to make table and field about the uav

### brand model and category get the value from the const.py file
class Uav(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    brand = models.CharField(max_length=50, choices=BRANDS, default=None)
    model = models.CharField(max_length=50, choices=MODELS, default=None)
    weight = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY, default=None)
    price = models.IntegerField()
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=user_listing_path)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']    
