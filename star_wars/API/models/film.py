from django.db import models
from django.utils.translation import gettext_lazy as _


class Film(models.Model):
    
    title = models.CharField('Title', max_length=100)
    opening_crawl = models.TextField('Opening paragraph')
    directors = models.JSONField('Directors', default=list)
    producers = models.JSONField('Producers', default=list)
    release_date = models.DateField('Release date')
    planets = models.ManyToManyField('Planet', related_name='films')
    img_url = models.URLField('Image URL', max_length=500, null=True)
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('Film')
        verbose_name_plural = _('Films')
