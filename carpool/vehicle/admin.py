from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'reg_number')

admin.site.register(Vehicle, VehicleAdmin)
