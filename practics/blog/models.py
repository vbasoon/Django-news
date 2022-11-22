from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default="Title")
    preview_text = models.CharField('Preview', max_length=250, default="Title")
    full_text = models.TextField('Text')
    date = models.DateTimeField('Data', default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорії")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"