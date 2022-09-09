from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import CustomUserManager
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    objects = CustomUserManager()

    # Set username field to None, because it was defined in AbstractUser & I don't want it
    username = None
    email = models.EmailField(_('email address'), unique=True)

    # The field named as the 'USERNAME_FIELD' for a custom user model must not be included in 'REQUIRED_FIELDS'
    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS[:]
    # Removing email from REQUIRED_FIELDS without changing parent REQUIRED_FIELDS class attribute
    REQUIRED_FIELDS.remove('email')
    USERNAME_FIELD = 'email'
