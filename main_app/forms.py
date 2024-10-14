from django import forms
from .models import ContactMessage, ConsultationRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ['name', 'phone', 'city', 'preferred_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'preferred_time': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('morning', 'Утро'),
                ('afternoon', 'День'),
                ('evening', 'Вечер')
            ]),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }