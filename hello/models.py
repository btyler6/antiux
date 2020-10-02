from django.db import models

# Create your models here.
class Donation(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

    name = models.CharField(null=True, max_length=30)
    phone = models.CharField(null=True, max_length=15)
    date = models.CharField(null=True, max_length=10)

    amount = models.IntegerField(null=True)

    address = models.CharField(null=True, max_length=50)
    county = models.CharField(null=True, max_length=20)
    state = models.CharField(null=True, max_length=2)
    coutry = models.CharField(null=True, max_length=10)
    zipcode = models.IntegerField(null=True)

    