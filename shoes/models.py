from pyexpat import model
from django.db import models

# Create your models here.
class ImageShoes (models.Model):
    id  = models.AutoField(primary_key=True)
    src = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.src}"
class CategoryShoes (models.Model):
    id  = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.type}"
class Shoes (models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    size = models.FloatField(null=True)
    sizeCountry = models.CharField(max_length=255,null=False)
    brand = models.CharField(max_length=255,null=False)
    color = models.CharField(max_length=255,null=False)
    weight = models.FloatField(null=True)
    manufactureDate=models.DateField(null=True)
    countryOrigin=models.CharField(max_length=255,null=False)
    department=models.CharField(max_length=255,null=False)
    upperMaterial=models.CharField(max_length=255,null=False)
    sideMaterial=models.CharField(max_length=255,null=False)
    liningMaterial=models.CharField(max_length=255,null=False)
    dimensions=models.CharField(max_length=255,null=False)
    CategoryShoes = models.ForeignKey(CategoryShoes, default = None, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.name}({self.brand})"
class ItemShoes (models.Model):
    id  = models.AutoField(primary_key=True)
    Shoes = models.ForeignKey(Shoes, default = None, on_delete = models.CASCADE)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    promo_text = models.CharField(max_length=255,null=False)
    decription = models.CharField(max_length=255,null=False)
    inventory = models.CharField(max_length=255,null=False)
    is_for_sale = models.BooleanField(default=True,null=False)
    def __str__(self):
        return f"{self.Shoes}"