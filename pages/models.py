from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Babie(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    brought_by = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    parent_name = models.CharField(max_length=100)
    fee = models.FloatField()
    period_of_stay = models.CharField(max_length=100)
    baby_number = models.CharField(max_length=10)
    age = models.IntegerField()
    sitter = models.CharField(max_length=100)#should attempt to make it foriegn key later

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_of_Birth = models.DateField()
    gender = models.CharField(max_length=6)
    next_of_kin = models.CharField(max_length=100)
    nin = models.CharField(max_length=100)
    recomender_name = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, null=True)
    level_of_education = models.CharField(max_length=100)
    sitter_number = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    on_duty = models.BooleanField(default=False)

class Pickup(models.Model):
    baby = models.CharField(max_length=100)#should attempt to make it foriegn key later
    name_of_person = models.CharField(max_length=100)
    comment = models.TextField(max_length=500, null=True)
    time = models.DateTimeField(auto_now_add=True)