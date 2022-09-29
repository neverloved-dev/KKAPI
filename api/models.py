from email.policy import default
from pickle import TRUE
from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    is_admin = models.BooleanField()
    is_super_admin = models.BooleanField()

class Course(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length = 500)
     teacher = models.ForeignKey(
            User,
            on_delete=models.CASCADE
     )
     student = models.ManyToManyField(User)
     

class Batch(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length = 500)
     course = models.ForeignKey(
         Course,
         on_delete=models.CASCADE
         )
     time = models.DurationField()
     url = models.URLField(default="")


class Task(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length = 500)
     description = models.TextField()
     teacher = models.ForeignKey(
         User,
         on_delete=models.CASCADE
         )
     course = models.ForeignKey(
            Course,
            on_delete=models.CASCADE
         )
         
class Forum(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    text = models.TextField()
    teacher = models.ForeignKey(
            User,
            on_delete=models.CASCADE
        )

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    filepath = models.FileField()
    teacher = models.ForeignKey(
            User,
            on_delete=models.CASCADE
        )