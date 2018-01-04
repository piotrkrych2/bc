from django.db import models


class Notification(models.Model):
    email = models.EmailField('Email', null=False, blank=False)
    message = models.TextField('Message', null=False, blank=False)
    viewed = models.BooleanField('Viewed', null=False, blank=False, default=False)
