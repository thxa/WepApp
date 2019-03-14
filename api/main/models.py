from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('categories', args=[self.slug])

    class Meta:
        ordering = ['name']



class Season(models.Model):
    name = models.CharField(max_length=70, blank=True, unique=True)
    photo_url = models.URLField(blank=True)
    slug = models.SlugField(blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name="seasones", blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('seasones', args=[self.slug])

    class Meta:
        ordering = ['created']



class Video(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True)
    photo_url = models.URLField(blank=True)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)
    # category = models.ManyToManyField(Category, related_name="videos", blank=False)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, related_name="episodes", blank=True, null=True)

    # next = connect with next video
    # prev = connect with prev video

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
