from django.db import models
from products.models import Feature


class Order(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=30, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=False)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=30, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    feature = models.ForeignKey(Feature, null=False)
    quantity = models.IntegerField(blank=False)

    def __str(self):
        return "{0} {1} @ {2}".format(self.feature.name, self.quantity, self.feature.price)

