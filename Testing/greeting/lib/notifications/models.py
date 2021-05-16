
from django.db import models
from account.models import User, Job, Application


class Notification(models.Model):
    MESSAGE = 'message'
    APPLICATION = 'application'

    CHOICES = (
        (MESSAGE, 'Message'),
        (APPLICATION, 'Application')
    )

    to_user = models.ForeignKey(
        User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='creatednotifications', on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job, related_name='notifications', on_delete=models.CASCADE)
    app = models.ForeignKey(
        Application, related_name='notifications', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']
