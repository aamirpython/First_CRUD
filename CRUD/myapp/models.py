from django.db import models

# Create your models here.
class Player(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    Email_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    
    password=models.CharField(max_length=100,blank=True,null=True)
    
    is_active=models.BooleanField(default=True)