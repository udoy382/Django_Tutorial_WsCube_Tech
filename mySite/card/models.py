from django.db import models

# Create your models here.

class Card(models.Model):
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()
    card_image = models.FileField(upload_to="cards/", max_length=250, null=True, default=None)