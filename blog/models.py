from django.db import models
from django.urls import reverse

# Create your models here.
class Article (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    author = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('blog:blog')