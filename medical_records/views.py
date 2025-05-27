from django.shortcuts import render, redirect
from .forms import MedicalRecordForm

def success_view(request):
    return render(request, 'medical_records/success.html')


def medical_form_view(request):
    if request.method == "POST":
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect after submission
    else:
        form = MedicalRecordForm()
    
    return render(request, 'medical_records/medical_form.html', {'form': form})
