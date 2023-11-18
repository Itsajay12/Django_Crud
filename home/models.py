from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=20)