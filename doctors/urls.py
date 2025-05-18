from django.contrib import admin
from django.urls import path
from patients.views import lit_patient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients', lit_patient)
]
