from django.contrib.auth.models import User
from django.db import models

class ConsumerModel(models.Model):
    GENDER_LIST = (
        ('male','MALE'),
        ('female','FEMALE'),
        ("lgbt",'LGBT')
    )
    REGISTER_AS = (
        ('consumer','CONSUMER'),
        ('manager','MANAGER')
    )

    uid = models.CharField(max_length=8)
    # profile_id = models.CharField(max_length = 5)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    birthdate = models.DateField(null=True,blank=True)
    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_LIST,null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to="images/")
    register_as = models.CharField(null=True, blank=False,choices=REGISTER_AS, max_length=12)

    def __str__(self):
        return self.name


