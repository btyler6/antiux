from django import forms
from .models import *

class CreditCardForm(ModelForm):
    card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)