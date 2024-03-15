from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    bestseller = models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ProductImages(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Images(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField()
    product_image = models.ForeignKey(ProductImages, on_delete=models.CASCADE)


