from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    published_ones = PublishedManager()

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            args=[
                self.published.year,
                self.published.strftime('%m'),
                self.published.strftime('%d'),
                self.slug
            ]
        )

    def __str__(self):
        return self.title
