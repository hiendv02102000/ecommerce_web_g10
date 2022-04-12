from django.db import models

# Create your models here.

class CategoryMobilePhone (models.Model):
    id  = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.type}"
class MobilePhone (models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    manufacturer_date = models.DateField(null=False)
    weight = models.CharField(max_length=255,null=False)
    color = models.CharField(max_length=255,null=False)
    warranty = models.CharField(max_length=255,null=False)

    dimensions = models.CharField(max_length=255,null=False)
    countryOrigin = models.CharField(max_length=255,null=False)
    cpu =  models.CharField(max_length=255,null=False)
    gpu =  models.CharField(max_length=255,null=False)
    storageSize =  models.CharField(max_length=255,null=False)
    screenSize =  models.CharField(max_length=255,null=False)
    screenResolution =  models.CharField(max_length=255,null=False)
    ramSize =  models.CharField(max_length=255,null=False)
    ramType =  models.CharField(max_length=255,null=False)
    connections =  models.CharField(max_length=255,null=False)
    interfaces =  models.CharField(max_length=255,null=False)
    battery =  models.CharField(max_length=255,null=False)
    os =  models.CharField(max_length=255,null=False)
    speaker =  models.CharField(max_length=255,null=False)
    frontCamera = models.CharField(max_length=255,null = False)
    rearCamera = models.CharField(max_length=255,null=False)

    CategoryMobilePhone = models.ForeignKey(CategoryMobilePhone, default = None, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.name}({self.manufacturer_date})"

class ItemMobilePhone(models.Model):
    id  = models.AutoField(primary_key=True)
    mobilePhone = models.ForeignKey(MobilePhone, default = None, on_delete = models.CASCADE)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    promoText = models.CharField(max_length=255,null=False)
    description = models.CharField(max_length=255,null=False)
    inventory = models.CharField(max_length=255,null=False)
    is_for_sale = models.BooleanField(default=True,null=False)
    def __str__(self):
        return f"{self.mobilePhone}"
