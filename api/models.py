from email.policy import default
from pickle import TRUE
from turtle import ondrag
from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 500)
    password = models.CharField(max_length = 500,null = False)
    


class Teacher(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length = 500)
     password = models.CharField(max_length = 500,null = False)

class Course(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length = 500)
     teacher = models.ForeignKey(
         Teacher,
         on_delete=models.CASCADE
         )
     students = models.ManyToManyField(Student)
     

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
         Teacher,
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
            Teacher,
            on_delete=models.CASCADE
        )