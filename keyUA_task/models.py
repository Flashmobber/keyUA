from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Entry(models.Model):
    date = models.DateField(auto_created=True, default=now())
    distance = models.IntegerField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def avg_speed(self):
        return round(self.distance / self.duration, 2)

    class Meta:
        verbose_name = "entry"
        verbose_name_plural = "entry's"

    def __str__(self):
        return self.date.isoformat()



