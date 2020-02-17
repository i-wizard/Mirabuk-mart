from django.contrib import admin
#import the class which wil be products
from .models import products
# Register your models here. using the register function which belongs to the admin.site object
admin.site.register(products)
#set path for all media in the settings file

