from django.db import models

# Create your models here.

# Contact Form

class Contact(models.Model):
    fullName=models.CharField(null=False,max_length=50)
    email=models.EmailField(null=False)
    address=models.CharField(null=False,max_length=200)
    subject=models.CharField(null=False,max_length=200)
    message=models.TextField()

#Post Form
class postModel(models.Model):
    title=models.CharField(null=False,max_length=200)
    desc=models.TextField(null=False)    