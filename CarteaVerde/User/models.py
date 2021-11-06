from django.db import models

# Create your models here.

class user(models.Model):
    id=models.AutoField(auto_created = True,primary_key = True)
    nume=models.CharField(max_length=200)
    #imagine=models.ImageField(upload_to="media/user",default="media/user/default.jpeg")
    locatie=models.CharField(max_length=200)
    date=models.TextField()
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    USERNAME_FIELD = ''
