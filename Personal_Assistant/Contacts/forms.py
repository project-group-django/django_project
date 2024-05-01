from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'birthday']
        
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = re.compile(r'^(\+\d{1,3}\s?)?((\(\d{1,3}\))|\d{1,3})[\s.-]?\d{1,4}[\s.-]?\d{1,4}$')
        if not pattern.match(phone):
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if not Contact.objects.filter(email=email).exists():
            raise forms.ValidationError("Please enter a valid email address.")
        return email
    
class ContactSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    
class DaysAheadForm(forms.Form):
    days_ahead = forms.IntegerField(label='Days ahead', min_value=1)