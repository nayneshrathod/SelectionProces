from django.db import models

import datetime
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'ProductApp'

    def __str__(self):
        return self.name
