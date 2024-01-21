from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Eatery(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    address = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('eatery-detail', kwargs={'pk': self.pk})
