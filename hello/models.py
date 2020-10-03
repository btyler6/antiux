from django.db import models

# Create your models here.
class Donation(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

    name = models.CharField("", null=True, max_length=30)
    phone = models.CharField("", null=True, max_length=15)
    date = models.CharField("", null=True, max_length=10)

    amount = models.CharField("", null=True, max_length=20)

    address = models.CharField("", null=True, max_length=50)
    county = models.CharField("", null=True, max_length=20)
    city = models.CharField("", null=True, max_length=20)
    state = models.CharField("", null=True, max_length=2)
    coutry = models.CharField("", null=True, max_length=10)
    country = models.CharField("", null=True, max_length=10)
    zipcode = models.CharField("", null=True, max_length=10)

""" class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label}) """