from django.db import models

# Create your models here.
# Table for storing the data of the contact us page

class Contact(models.Model):
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)