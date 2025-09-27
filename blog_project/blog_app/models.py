from django.db import models

# Create your models here.

class Post(models.Model):
    serial_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=15)
    author = models.CharField(max_length=50)
    slug = models.TextField()
    time_stamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author