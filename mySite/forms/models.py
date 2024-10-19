from django.db import models

# Create your models here.

class Forms(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100)