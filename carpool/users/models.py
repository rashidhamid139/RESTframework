from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


GENDER_OPTIONS = (
    ('female', 'Female'),
    ('male', 'Male'),
    ("wont-say", "Won't say"),
)

class User(AbstractUser):
    gender = models.CharField(null=True, blank=True, max_length = 30, choices = GENDER_OPTIONS, default="wont-say", verbose_name= _('Gender'), help_text= "User's Gender")
    birth_date = models.DateField(null=True, blank=True, verbose_name='Date of Birth', help_text=_('Date of birth'))


    def __str__(self):
        return self.email


    class Meta:
        verbose_name = _('User')
        verbose_name_plural= _('Users')



