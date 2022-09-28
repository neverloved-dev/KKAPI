from django.db import models

# Create your models here.
class Admin(models.Model):
   id = models.IntegerField(primary_key = True)
   name = models.CharField(max_length=80)
   password = models.CharField(max_length=80)



class SuperAdmin(models.Model):
   id = models.IntegerField(primary_key = True)
   name = models.CharField(max_length=80)
   password = models.CharField(max_length=80)