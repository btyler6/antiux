from django import forms
from .models import Donation
from django.core.exceptions import ValidationError

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = (
            'address',
            'name',
            'phone', 
            'amount',
            'country', 
            'zipcode',
            'date',  
            'city', 
            'state', 
            )
"""     def clean_zipcode(self):
        data = self.cleaned_data['zipcode']
        if data[5] != '-':
            msg = "must use format xxxxx-xxxx"
            self.add_error('zip_format', msg) """
    #card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)