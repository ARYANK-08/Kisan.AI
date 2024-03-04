from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_total = models.IntegerField()
    date_bought = models.DateField()
    date_expiration = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_remaining = models.IntegerField()

    def __str__(self):
        return self.name
