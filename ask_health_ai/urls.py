
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import ai_answer_view
from .views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userauths.urls')),

    path("", include('core.urls')),
    path("ask-ai/", ai_answer_view, name="ask_ai"),
    path("contact/", contact_view, name="contact"),
    path("med/", include('medical_records.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
