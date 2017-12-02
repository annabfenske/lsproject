from django.db import models
from django.conf import settings

class lostNYUID(models.Model):
    net_id = models.CharField("Net ID", max_length=10, blank=False)
    time_lost = models.DateTimeField(primary_key=True, blank=False)

    def __str__(self):
        return 'time lost' + str(self.time_lost)
