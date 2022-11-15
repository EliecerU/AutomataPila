
from __future__ import unicode_literals
from django.db import models

class Validate(models.Model):

    word = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self): #Python 2
        return self.word
    def __str__(self): # Python 3
        return self.word
