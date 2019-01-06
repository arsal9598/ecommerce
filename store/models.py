from django.db import models
from django.conf import settings
import decimal

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, help_text="Enter product name")
    description = models.TextField(help_text="Enter product description")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Enter product price")
    image = models.ImageField(upload_to='photos/')
    available = models.BooleanField(default=True)
    address = models.CharField(max_length=500, help_text="Address you have to ship this product to", blank=True)
    email = models.EmailField(blank=True, null=True, help_text="Email of the customer")

    @property
    def price_in_cents(self):
        return self.price * 100

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
