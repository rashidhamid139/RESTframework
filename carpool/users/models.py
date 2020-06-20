from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


GENDER_OPTIONS = (
    ('female', 'Female'),
    ('male', 'Male'),
    ('wont-say', "Won't say"),
)

class User(AbstractUser):
    gender = models.CharField(null=True, blank=True, max_length=30, choices=GENDER_OPTIONS, default='wont-say', verbose_name=_('Gender'), help_text = _('User"s Gender'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Date of birth'), help_text=_('Date of birth'))
    profile_pic = models.ImageField(upload_to='profiles/', verbose_name=_('Profile_Image'), null=True, blank=True)
    def __str__(self):return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    
    def save(self, *args, **kwargs):
        if self.birth_date:
            print("Test")
            if self.birth_date > date.today():
                raise ValidationError("Birth date cannot be in the future")
            age = relativedelta(date.today(), self.birth_date).years
            print(age)
            if age < 18:
                raise ValidationError("User should be 18 years or older")
        super(User, self).save(*args, **kwargs)

class Vehicle(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='vehicles', verbose_name=_('Owner'))
    make = models.CharField(max_length=30, verbose_name=_('Make'), null=False, blank=False)
    model = models.CharField(max_length=30, verbose_name=_('Model'), null=False, blank=False)
    reg_number = models.CharField(max_length=30, verbose_name=_('Registration Number'), null=False, blank=False)
    image = models.ImageField(upload_to='vehicles/', verbose_name=_('Image'), null=True, blank=True)

    def __str__(self):
        return f'{self.make} {self.model} owned by {self.user}'

    class Meta:
        verbose_name=_('Vehicle')
        verbose_name_plural = _('Vehicles')

class Place(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

class Trip(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='trips', null=False, blank=False, verbose_name=_('Driver'))
    origin = models.ForeignKey(Place, on_delete=models.CASCADE, null=False, blank=False, related_name='trip_origins', verbose_name=_('From'))
    destination = models.ForeignKey(Place, on_delete=models.CASCADE, null=False, blank=False, related_name='trip_destinations', verbose_name=_('To'))
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False, blank=False, related_name='trip_vehicles', verbose_name=_('Vehicle'))
    trip_date = models.DateField(null=False, blank=False, verbose_name=_('Trip date'))
    num_seats = models.IntegerField()


    def save(self, *args, **kwargs):
        if self.origin == self.destination:
            raise ValidationError("Origin and destination cannot be the same")
        if self.trip_date < date.today():
            raise ValidationError('Trip date cannot be in the past')
        super(Trip, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.origin} to {self.destination} by {self.user}'

    class Meta:
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')

