from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import CustomUserManager


class User(AbstractUser):
    objects = CustomUserManager()

    # Email as a username field must be unique
    # I've just added a unique constraint to email field instead of defining again email field
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='email')
        ]

    # The field named as the 'USERNAME_FIELD' for a custom user model must not be included in 'REQUIRED_FIELDS'
    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS[:]
    # Removing email from REQUIRED_FIELDS without changing parent REQUIRED_FIELDS class attribute
    REQUIRED_FIELDS.remove('email')
    USERNAME_FIELD = 'email'
