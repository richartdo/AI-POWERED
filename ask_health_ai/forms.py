# forms.py
from django import forms

class MedicalAIQueryForm(forms.Form):
    AGE_GROUP_CHOICES = [
        ('', 'Select Age Group'),
        ('0-12', 'Child (0-12)'),
        ('13-19', 'Teenager (13-19)'),
        ('20-39', 'Young Adult (20-39)'),
        ('40-59', 'Middle Age (40-59)'),
        ('60+', 'Senior (60+)')
    ]

    URGENCY_CHOICES = [
        ('', 'Select Urgency Level'),
        ('low', 'Non-urgent (General Query)'),
        ('medium', 'Moderate (Seeking Clarity)'),
        ('high', 'Urgent (Immediate Concern)')
    ]

    # The 5 essential fields
    age_group = forms.ChoiceField(
        choices=AGE_GROUP_CHOICES,
        label="Age Group",
        required=True
    )
    
    main_symptoms = forms.CharField(
        label="Main Symptoms",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=True,
        help_text="Describe your main symptoms in detail"
    )

    symptom_duration = forms.CharField(
        label="Symptom Duration",
        max_length=100,
        required=True,
        help_text="How long have you been experiencing these symptoms?"
    )

    urgency_level = forms.ChoiceField(
        choices=URGENCY_CHOICES,
        label="Urgency Level",
        required=True
    )

    question = forms.CharField(
        label="Specific Question",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=True,
        help_text="What specific medical advice are you seeking?"
    )

# views.py
from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai
from .forms import MedicalAIQueryForm

def ai_answer_view(request):
    answer = None
    
    # Configure the API key
    genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)

    if request.method == "POST":
        form = MedicalAIQueryForm(request.POST)
        if form.is_valid():
            # Construct a simplified prompt for the AI
            prompt = f"""
            Patient Information:
            - Age Group: {form.cleaned_data['age_group']}
            
            Current Situation:
            - Main Symptoms: {form.cleaned_data['main_symptoms']}
            - Duration: {form.cleaned_data['symptom_duration']}
            - Urgency Level: {form.cleaned_data['urgency_level']}
            
            Specific Question: {form.cleaned_data['question']}
            
            Please provide a detailed medical information response based on the above context. 
            Include potential causes, recommended actions, and when to seek immediate medical attention if necessary.
            Note: This is for informational purposes only and does not replace professional medical advice.
            """

            # Generate AI response
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)
            answer = response.text if response else "No response received."

            # Add a medical disclaimer to the answer
            disclaimer = "\n\nDISCLAIMER: This information is for educational purposes only and should not replace professional medical advice. Please consult with a healthcare provider for proper diagnosis and treatment."
            answer = answer + disclaimer

    else:
        form = MedicalAIQueryForm()

    return render(request, "ai_answer.html", {"form": form, "answer": answer})
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
