from django.db import models
from datetime import datetime, date


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default="Title")
    preview_text = models.CharField('Preview', max_length=250, default="Title")
    full_text = models.TextField('Text')
    date = models.DateTimeField('Data', auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
