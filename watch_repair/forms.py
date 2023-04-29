from django import forms
from django_countries.fields import CountryField
from .models import WatchRepair


class WatchRepairForm(forms.ModelForm):
    class Meta:
        model = WatchRepair
        fields = ['full_name', 'email', 'phone_number',
                  'quartz', 'mechanical', 'chronograph', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'placeholder': 'Full Name'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email Address'})
        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': 'Phone Number'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Brand/Case Reference/Fault'})
