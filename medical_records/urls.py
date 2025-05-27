from django.urls import path
from .views import medical_form_view, success_view

urlpatterns = [
    path('medical-form/', medical_form_view, name='medical_form'),
    path('success/', success_view, name='success_page'),
]
