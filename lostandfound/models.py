from django.db import models
from django.conf import settings

class User(models.Model):
    net_id = models.CharField("Net ID", max_length=10, blank=False, primary_key=True)
    time_lost = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return 'time lost' + str(self.time_lost)
