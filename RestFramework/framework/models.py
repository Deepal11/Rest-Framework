from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(default=0)
    name = models.CharField(max_length=30) 
    mobile = models.BigIntegerField(default=0)