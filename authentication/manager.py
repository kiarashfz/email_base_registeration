from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    # Username is a required field in protected method _create_user in UserManager
    # I want email base registration without username
    # I didn't override _create_user method because it's protected
    # Now username is an optional field that filled by email
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = email
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = email
        return super().create_user(username, email, password, **extra_fields)

