from django import forms
from .models import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'pre_existing_conditions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'List any pre-existing conditions'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Any known allergies?'}),
            'current_medications': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'List your current medications'}),
            'previous_surgeries': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mention any previous surgeries'}),
            'family_medical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Family medical history'}),
            'symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe your symptoms'}),
            'duration_of_symptoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How long have symptoms lasted?'}),
            'severity': forms.Select(attrs={'class': 'form-control'}),
            'preferred_doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional: Preferred doctor'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter emergency contact name'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter emergency contact phone'}),
            'insurance_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insurance provider (if applicable)'}),
        }
