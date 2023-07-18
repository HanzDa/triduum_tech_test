from django.db import models
from django.utils.translation import gettext_lazy as _


class Planet(models.Model):
    
    name = models.CharField('Planet Name', max_length=100)
    diameter = models.CharField('Diameter', max_length=15)
    gravity = models.IntegerField('Gravity')
    population = models.IntegerField('Population')
    climate = models.CharField('Climate', max_length=30)
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Planet')
        verbose_name_plural = _('Planets')
