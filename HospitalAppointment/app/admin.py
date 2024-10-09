from django.contrib import admin
from . models import user,user_contact_details,Appointment,Payment
# Register your models here.
admin.site.register(user)
admin.site.register(user_contact_details)
admin.site.register(Appointment)
admin.site.register(Payment)
