from django.db import models

# Create your models here.
class products(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='img/mirabuk')
    price=models.IntegerField()
    #(done once)install pillows app with pip to handle image upload
    #mention your app name in the 'installed apps' section of your settings file
    #after this you have to make maigrations with the cmd'python manage.py makemigrations

