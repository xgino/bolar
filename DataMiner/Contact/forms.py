from django import forms
from .models import Quote, Service

class QuoteForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), empty_label="Select Service")
    
    class Meta:
        model = Quote
        fields = ['name', 'company', 'email', 'phone', 'kvk', 'website', 'service', 'remarks']


class EmailForm(forms.Form):
    email = forms.EmailField(label='Email')