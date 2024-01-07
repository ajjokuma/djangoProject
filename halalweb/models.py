from django.db import models
from django.utils import timezone
# Create your models here.

class Eatery(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    address = models.TextField()

    def __str__(self):
        return self.title