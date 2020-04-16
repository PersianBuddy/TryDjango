from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) # it's not required
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.TextField(blank=False, default="Default Summary") # it's required

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'product_id':self.id })