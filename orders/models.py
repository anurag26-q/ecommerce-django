from django.db import models
from users.models import User
from products.models import Product

# Create your models here.

class Promo(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    items = models.IntegerField()
    promo_id = models.ForeignKey(Promo, on_delete=models.CASCADE)




