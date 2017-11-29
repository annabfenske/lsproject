from django.db import models

# Create your models here.

class User(models.Model):
    net_id = models.CharField("Net ID", max_length=10, blank=False, null=False, primary_key=True)
    n_number = models.CharField("N#", max_length=10, blank=False, null=False)
    first_name = models.CharField("First Name", max_length=250, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=250, blank=False, null=False)
    nyu_email = models.EmailField(max_length=254)
    id_lost = models.BooleanField(blank=False, null=False, default=False)
