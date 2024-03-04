from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    farmer_name = models.CharField(max_length=100, null=True, blank=True)  # Add field for farmer's name
    farmer_contact = models.CharField(max_length=15)
    date_of_posting = models.DateField(default=timezone.now,null=True, blank=True)  # Add field for date of posting
    location = models.CharField(max_length=100,null=True, blank=True)  # Add field for location

    def __str__(self):
        return self.name
