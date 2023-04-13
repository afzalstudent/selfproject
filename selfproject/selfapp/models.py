from django.db import models
from django import urls

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        db_table="department"

    def __str__(self):
        return self.name



class Courses(models.Model):
    name = models.CharField(max_length=250, unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        db_table="courses"

    def __str__(self):
        return self.name

