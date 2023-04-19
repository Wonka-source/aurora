from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                'billing_address1', 'billing_address2',
                'shipping_address1', 'shipping_address2',
                'delivery_method',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'billing_address1': 'Billing Address 1',
            'billing_address2': 'Billing Address 2',
            'shipping_address1': 'Shipping Address 1',
            'shipping_address2': 'Shipping Address 2',
            'delivery_method': 'Delivery Method',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False