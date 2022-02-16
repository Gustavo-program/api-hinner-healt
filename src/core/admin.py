from django.contrib import admin

from .models import Especiality, Testimonial, Doctor, Patient, Appointment


admin.site.register(Especiality)
admin.site.register(Testimonial)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
