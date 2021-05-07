from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stock(models.Model):
    identifier = models.CharField(primary_key = True, max_length=20)
    day_high = models.FloatField()
    day_low = models.FloatField()
    current = models.FloatField()
    change = models.FloatField()
    pchange = models.FloatField()
    pchange365 = models.FloatField()
    last_update = models.DateTimeField(auto_now=False)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    class Meta:
        ordering = ['identifier']

    def __str__(self):
        return self.identifier