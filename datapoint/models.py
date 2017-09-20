# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Datapoint(models.Model):
    """
    Create table 'Datapoint' in Db with fields:
      - freq
      - name
      - date
      - value
    """
    FREQ_CHOICES = (
        ('a', 'a'),
        ('q', 'q'),
        ('m', 'm'),
        ('w', 'w'),
        ('d', 'd'),
    )

    freq = models.CharField(
        max_length=1,
        choices=FREQ_CHOICES,
        default='a',
    )
    name = models.CharField(max_length=64, null=False)
    date = models.DateField(null=False)
    value = models.FloatField(null=False)

    class Meta:
        unique_together = ('freq', 'name', 'date')
