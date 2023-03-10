from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


### It connects with User model and provide us new fields to use
### And write this model to the db
class UserProfile(models.Model):
    Male = 'Male'
    Female = 'Female'
    Other = "Other"
    Gender = ((Male,'Male'),(Female,"Female"),(Other,"Other"))
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    phone_number = models.CharField(max_length=11,verbose_name='Phone Number',blank=True)
    gender = models.CharField(max_length=6,default=3,verbose_name='Gender',choices=Gender,blank=True)


    def __str__(self):
        return self.user.username
   
### POST SIGNAL
### It provide us to fill the fields which are in the UserProfile Model
### And It can make this process at the same time with registering the new user
def create_profile(sender,**kwargs):
    if kwargs['created']:
        profile = UserProfile.objects.create(
            user = kwargs['instance']
        )
    
post_save.connect(create_profile,sender=User)
