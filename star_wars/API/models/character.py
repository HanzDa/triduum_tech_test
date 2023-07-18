from django.db import models
from django.utils.translation import gettext_lazy as _


class Character(models.Model):
    
    GENDER_CHOICES = (('male', 'Male'),
                      ('female', 'Female'),
                      ('unknown', 'Unknown'),)
    
    name = models.CharField('Name', max_length=100)
    gender = models.CharField('Gender', choices=GENDER_CHOICES, max_length=7)
    age = models.IntegerField('Age')
    skin_color = models.CharField('Skin color', max_length=30)
    eye_color = models.CharField('Eye color', max_length=30)
    height = models.IntegerField('Height')
    mass = models.IntegerField('Mass')
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Character')
        verbose_name_plural = _('Characters')
