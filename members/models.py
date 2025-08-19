from django.db import models

# Create your models here.
class Member(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    age=models.IntegerField()
    slug = models.SlugField(default='',null=False)