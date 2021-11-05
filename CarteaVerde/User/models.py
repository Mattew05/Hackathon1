from django.db import models

# Create your models here.

class user(models.Model):
    id=models.AutoField(auto_created = True,primary_key = True,)
    nume=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    imagine=models.ImageField(default="media/user/default.jpeg",upload_to='media/user')
    locatie=models.CharField(max_length=200)
    date=models.TextField()
    email=models.CharField(max_length=200)
    parola=models.CharField(max_length=200)