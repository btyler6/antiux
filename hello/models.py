from django.db import models

# Create your models here.
class Donation(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

    name = models.CharField(null=True, max_length=30, default='please do not forget to include your full name here')
    phone = models.CharField(null=True, max_length=15, default='please use the format: +x(xxx)xxx-xxxx and do not include any spaces')
    date = models.CharField(null=True, max_length=10, default='please provide 10 characters i.e. 01/10/2020')

    amount = models.CharField(null=True, max_length=20, default='please do not include any special characters or spaces')

    address = models.CharField(null=True, max_length=50)
    county = models.CharField(null=True, max_length=20)
    city = models.CharField(null=True, max_length=20)
    state = models.CharField(null=True, max_length=2, default='please provide state initials i.e. NY')
    coutry = models.CharField(null=True, max_length=10)
    country = models.CharField(null=True, max_length=10)
    zipcode = models.CharField(null=True, max_length=10, default='please use for format: xxxxx-xxxx')

    