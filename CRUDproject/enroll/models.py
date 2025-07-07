from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50,null=False)
    dob=models.DateField(null=False)
    address=models.CharField(null=False)
    phoneNumber=models.CharField(max_length=10,null=False)
    email=models.EmailField(null=False)
    course=models.CharField(null=False)
    gender=models.CharField(null=False)
    
    