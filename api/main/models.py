from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('videos', args=[self.slug])

    class Meta:
        ordering = ['name']


class Video(models.Model):
    name = models.CharField(max_length=30)
    photo_url = models.URLField(blank=True)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE , related_name="videos")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('videos', args=[self.slug])

    class Meta:
        ordering = ['created']
