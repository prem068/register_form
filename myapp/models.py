from django.db import models
from django.core.exceptions import ValidationError



# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    dob=models.DateField()
    phno=models.IntegerField()
    addr=models.CharField(max_length=30)

    def __str__(self):
        return self.name