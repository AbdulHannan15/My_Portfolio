from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images')
    link = models.URLField(blank=True)