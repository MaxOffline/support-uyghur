from django.db import models

# Create your models here.
class Vote (models.Model):
    agree = models.IntegerField(blank = False)
    disagree = models.IntegerField(blank = False)

    def __str__(self):
        return "Vote"

class Token (models.Model):
    token = models.CharField( max_length=100)

    def __str__(self):
        return "Token"