from django.db import models

# Create your models here.

class Log(models.Model):
    time = models.DateTimeField('date published')
    cpu = models.IntegerField()
    ram = models.IntegerField()
