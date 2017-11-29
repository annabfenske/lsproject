from django.db import models

# Create your models here.

class User(models.Model):
    net_id = models.CharField("Net ID", max_length=10, blank=False, null=False, primary_key=True)
    time_lost = models.DateTimeField("Time Lost")
