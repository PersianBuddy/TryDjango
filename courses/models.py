from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    participants = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('courses:courses_list')