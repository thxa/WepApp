from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    # owner = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True, blank=False)
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
    owner = models.ForeignKey(User, related_name='seasones', on_delete=models.CASCADE)
    name = models.CharField(max_length=70, blank=False, unique=True, null=False)
    number_of_episodes = models.PositiveSmallIntegerField(default=1, blank=True)
    photo_url = models.URLField(blank=True)
    # photo = models.ImageField()
    slug = models.SlugField(blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name="seasones", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # self.photo.upload_to(f'/season/{self.name}/')
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('seasones', args=[self.slug])

    class Meta:
        ordering = ['created']


class Video(models.Model):
    owner = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    # name = models.PositiveSmallIntegerField(blank=False)
    photo_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)
    # category = models.ManyToManyField(Category, related_name="videos", blank=False)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="episodes", null=True)

    # next = connect with next video
    # prev = connect with prev video

    def __str__(self):
        return f"{self.season.name}-{self.name}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(f"{self.season.name}-{self.name}")

        if not self.photo_url:
            self.photo_url = self.season.photo_url

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('videos', args=[self.slug])

    class Meta:
        ordering = ['created']
