from pyexpat import model
from django.db import models

# Create your models here.
class CategoryClothes (models.Model):
    id  = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.type}"

class Clothes (models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    brand = models.CharField(max_length=255,null=False)
    color = models.CharField(max_length=255,null=False)
    manufacturerDate = models.DateField(null=False)
    material = models.CharField(max_length=255,null=False)
    department = models.CharField(max_length=255,null=False)
    size = models.CharField(max_length=255,null=False)
    sizeCountry = models.CharField(max_length=255,null=False)
    washingType = models.CharField(max_length=255,null=False)
    color = models.CharField(max_length=255,null=False)
    weight = models.FloatField(null=True)
    fitType = models.CharField(max_length=255,null=False)
    closureType = models.CharField(max_length=255,null=False)
    dimensions = models.CharField(max_length=255,null=False)
    countryOrigin = models.CharField(max_length=255,null=False)
    CategoryClothes = models.ForeignKey(CategoryClothes, default = None, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.name}({self.manufacturerDate})"

class ItemClothes(models.Model):
    id  = models.AutoField(primary_key=True)
    Clothes = models.ForeignKey(Clothes, default = None, on_delete = models.CASCADE)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    promoText = models.CharField(max_length=255,null=False)
    decription = models.CharField(max_length=255,null=False)
    inventory = models.CharField(max_length=255,null=False)
    isForSale = models.BooleanField(default=True,null=False)
    def __str__(self):
        return f"{self.Clothes}"