# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Address(models.Model):
	street = models.TextField()
	province = models.TextField()
	city = models.TextField()