from django.db import models
from django.utils import timezone


class Feature(models.Model):
    name = models.CharField(max_length=20, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(default='images/default.jpg', upload_to='images')

    def __str__(self):
        return self.name


