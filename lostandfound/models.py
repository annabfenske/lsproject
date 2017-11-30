from django.db import models
from django.forms import ModelForm

class User(models.Model):
    net_id = models.CharField("Net ID", max_length=10, blank=False, primary_key=True)
    time_lost = models.DateTimeField()
