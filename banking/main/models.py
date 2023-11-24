from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class District(models.Model):
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.branch


class Continue_register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default=None)
    dob = models.DateField(default=None)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=None)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100, default=None, choices=[('current_account','Current account'),('savings','Savings account'),('fd','Fixed deposit accoutnt'),('nri','NRI accounts')])
    materials_provide = models.CharField(max_length=100, default=None)



