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
            'cardnum',
            'state', 
            )
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'first and last name'}),
            'address' : forms.TextInput(attrs={'placeholder': 'street address'}),
            'phone' : forms.TextInput(attrs={'placeholder': 'phone number'}), 
            'amount' : forms.TextInput(attrs={'placeholder': 'donation amount'}),
            'country' : forms.TextInput(attrs={'placeholder': 'country'}), 
            'zipcode' : forms.TextInput(attrs={'placeholder': 'zip code'}),
            'date' : forms.TextInput(attrs={'placeholder': 'today\'s date'}),  
            'city' : forms.TextInput(attrs={'placeholder': 'city'}), 
            'cardnum' : forms.TextInput(attrs={'placeholder': 'credit card number'}),
            'state' : forms.TextInput(attrs={'placeholder': 'state'}),
        }
"""     def clean_zipcode(self):
        data = self.cleaned_data['zipcode']
        if data[5] != '-':
            msg = "must use format xxxxx-xxxx"
            self.add_error('zip_format', msg) """
    #card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)