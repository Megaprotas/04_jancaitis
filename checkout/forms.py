from django import forms
from .models import Order, OrderLineItem


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2035)]

    credit_card_number = forms.CharField(label='Credit/Debit Card Number', required=False)
    cvv = forms.CharField(label='CVV', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = {'full_name', 'phone_number', 'country', 'postcode', 'city', 'address1', 'address2', 'county'}


