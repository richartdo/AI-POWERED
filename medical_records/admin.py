from django.contrib import admin
from .models import *

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display=['name','age','gender','phone', 'email','pre_existing_conditions','allergies','current_medications','previous_surgeries','family_medical_history','symptoms','duration_of_symptoms','severity','preferred_doctor']



admin.site.register(MedicalRecord, MedicalRecordAdmin)
