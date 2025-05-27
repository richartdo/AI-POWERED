from django.shortcuts import render
import google.generativeai as genai
from .forms import  MedicalAIQueryForm
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings



# views.py
from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai
from .forms import MedicalAIQueryForm

def ai_answer_view(request):
    answer = None
    
    genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)

    if request.method == "POST":
        form = MedicalAIQueryForm(request.POST)
        if form.is_valid():
            prompt = f"""
            Based on the following patient information, provide a VERY CONCISE medical information response (total response must be under 200 words):

            Patient Information:
            - Age Group: {form.cleaned_data['age_group']}
            - Main Symptoms: {form.cleaned_data['main_symptoms']}
            - Duration: {form.cleaned_data['symptom_duration']}
            - Urgency Level: {form.cleaned_data['urgency_level']}
            
            Question: {form.cleaned_data['question']}

            Structure your response exactly like this:

            QUICK SUMMARY (1-2 sentences only):
            [your brief summary]

            LIKELY CAUSES:
            • [cause 1]
            • [cause 2]
            • [cause 3]

            RECOMMENDED ACTIONS:
            • [action 1]
            • [action 2]
            • [action 3]

            WHEN TO SEEK IMMEDIATE CARE:
            • [warning 1]
            • [warning 2]

            Keep everything extremely concise. Use bullet points only. No paragraphs except for the quick summary.
            """

            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)
            raw_answer = response.text if response else "No response received."

            # Format the answer with styled sections
            formatted_answer = f"""
            <div class="section summary">
                <h3>Quick Summary</h3>
                {raw_answer}
            </div>
            """
            
            answer = formatted_answer

    else:
        form = MedicalAIQueryForm()

    return render(request, "ai_answer.html", {"form": form, "answer": answer})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            # Email message content
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email
            send_mail(
                subject,
                email_message,
                settings.EMAIL_HOST_USER,  # From email
                ["ngumodaniel74@gmail.com"],  # Replace with your email
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")  # Redirect to the contact page after submission

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
