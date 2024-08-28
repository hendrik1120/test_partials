from django.db import models

# Create your models here.

class TestModel(models.Model):
    text = models.CharField(max_length=100)
