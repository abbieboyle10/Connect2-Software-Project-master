from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Job)
def post_save_job(sender, instance, created, **kwargs):
    employer_ = instance.employer
    if instance.status == 'applied':

        employer_.applicants.add(candidate.tag)
        candidate_.save()
        job_.save()
