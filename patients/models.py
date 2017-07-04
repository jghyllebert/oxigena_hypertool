from django.db import models
from django.utils.translation import ugettext_lazy as _

from clients.models import BaseDetails, Client

GENDERS = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('O', _('Other'))
)


class Patient(BaseDetails):
    doctor = models.ForeignKey(Client)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDERS)
    image = models.ImageField(upload_to='patients/', null=True)
