from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Report(models.Model):
    objects = models.Manager()
    input_id = models.CharField(max_length=50, null=True, default='비어있음')
    input_pw = models.CharField(max_length=50, default=0, null=True, blank=True)
