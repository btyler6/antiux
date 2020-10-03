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
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'please include your first and last name'}),
            'address' : forms.TextInput(attrs={'placeholder': 'please enter your street address'}),
            'phone' : forms.TextInput(attrs={'placeholder': 'please use the format: +x(xxx)xxx-xxxx to give your phone number and do not include any spaces'}), 
            'amount' : forms.TextInput(attrs={'placeholder': 'please enter your donation amount and do not include any special characters or spaces'}),
            'country' : forms.TextInput(attrs={'placeholder': 'please provide the country you live in'}), 
            'zipcode' : forms.TextInput(attrs={'placeholder': 'please use for format: xxxxx-xxxx to provide your zip code'}),
            'date' : forms.TextInput(attrs={'placeholder': 'please provide 10 characters for today\'s date i.e. 01/10/2020'}),  
            'city' : forms.TextInput(attrs={'placeholder': 'plase provide the city that you live in'}), 
            'state' : forms.TextInput(attrs={'placeholder': 'please provide state initials i.e. NY'}),
        }
"""     def clean_zipcode(self):
        data = self.cleaned_data['zipcode']
        if data[5] != '-':
            msg = "must use format xxxxx-xxxx"
            self.add_error('zip_format', msg) """
    #card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)