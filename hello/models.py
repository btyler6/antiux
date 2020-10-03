from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#validators
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
# Create your models here.
class Donation(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

    name = models.CharField("", null=True, blank=False, max_length=30)
    phone = models.IntegerField("", null=True, blank=False, max_length=15)
    date = models.IntegerField("", null=True, blank=False, max_length=10)

    amount = models.IntegerField("", null=True, blank=False, max_length=20)
    cardnum = models.IntegerField("", null=True, blank=False)

    address = models.CharField("", null=True, blank=False, max_length=50)
    county = models.CharField("", null=True, blank=False, max_length=20)
    city = models.CharField("", null=True, blank=False, max_length=20)
    state = models.CharField("", null=True, blank=False, max_length=2)
    coutry = models.CharField("", null=True, blank=False, max_length=10)
    country = models.CharField("", null=True, blank=False, max_length=10)
    zipcode = models.IntegerField("", null=True, blank=False, max_length=10)

""" class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label}) """