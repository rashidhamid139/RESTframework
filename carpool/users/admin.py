from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Vehicle, Place, Trip
CustomUser = get_user_model()
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [ 'username', 'first_name', 'last_name', 'email', 'gender', 'birth_date']
    add_fieldsets = (
        (
            'User info',
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'email',
                    'password1',
                    'password2',
                    'gender',
                    'birth_date',
                    'profile_pic'
                ),
            },
        ),
    )
    fieldsets = (
        (
            'User info',
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'email',
                    'gender',
                    'birth_date',
                    'profile_pic'
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'reg_number')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_date', 'origin', 'destination', 'user',)