from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from authentication.models import User
import logging

logger = logging.getLogger('django')


@receiver(post_save, sender=User)
def log_modified_user(sender, instance, created, **kwargs):
    logger.info(msg=f'modified user email: {instance.email}')


@receiver(post_delete, sender=User)
def log_deleted_user(sender, instance, **kwargs):
    logger.info(msg=f'deleted user email: {instance.email}')
