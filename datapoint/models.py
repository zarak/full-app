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
    freq = models.CharField(max_length=64, null=False)
    name = models.CharField(max_length=64, null=False)
    date = models.DateField()
    value = models.FloatField()
