from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    loc1 = models.CharField(max_length=100)
    loc2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class User(models.Model):
    # user = models.OneToOneField( on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name




