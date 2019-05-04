from django.db import models

class task(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.CharField(max_length=100)
