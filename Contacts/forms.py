from django import forms
from .models import Contact
import re
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'birthday']
        
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = re.compile(r'^(\+\d{1,3}\s?)?((\(\d{1,3}\))|\d{1,3})[\s.-]?\d{1,4}[\s.-]?\d{1,4}$')
        if not pattern.match(phone):
            raise forms.ValidationError("Будь ласка введіть дійсний номер телефону.")
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValidationError("Будь ласка, введіть дійсну адресу електронної пошти.")
        if '.' not in email.split('@')[1]:
            raise ValidationError("Будь ласка, введіть дійсну адресу електронної пошти.")
        if Contact.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Ця електронна адреса вже використана.")
        return email
        
class ContactSearchForm(forms.Form):
    query = forms.CharField(label='Пошук', max_length=100)
    
class DaysAheadForm(forms.Form):
    days_ahead = forms.IntegerField(label='Днів до', min_value=1)