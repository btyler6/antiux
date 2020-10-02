from django import forms
from .models import Donation

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
    #card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)