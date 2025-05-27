from django.db import models

class MedicalRecord(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    SEVERITY_CHOICES = [
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Severe', 'Severe'),
    ]
    
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    pre_existing_conditions = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    previous_surgeries = models.TextField(blank=True, null=True)
    family_medical_history = models.TextField(blank=True, null=True)
    symptoms = models.TextField()
    duration_of_symptoms = models.CharField(max_length=255)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    preferred_doctor = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=15)
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.symptoms[:30]}"
