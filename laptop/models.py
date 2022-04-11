from pyexpat import model
from django.db import models

# Create your models here.
# class Publisher (models.Model):
#     id  = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255,null=False)
#     address = models.CharField(max_length=255,null=False)
#     def __str__(self):
#         return f"{self.name}({self.address})"
class CategoryLaptop (models.Model):
    id  = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.type}"
class Laptop (models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    # summary = models.CharField(max_length=255,null=False)
    manufacturer_date = models.DateField(null=False)
    weight = models.CharField(max_length=255,null=False)
    color = models.CharField(max_length=255,null=False)
    warranty = models.CharField(max_length=255,null=False)

    # num_of_pages = models.IntegerField(null=True)
    dimensions = models.CharField(max_length=255,null=False)
    countryOrigin = models.CharField(max_length=255,null=False)
    # weight = models.FloatField(null=True)
    cpu =  models.CharField(max_length=255,null=False)
    gpu =  models.CharField(max_length=255,null=False)
    storageSize =  models.CharField(max_length=255,null=False)
    storageType = models.CharField(max_length=255, null=False)
    screenSize =  models.CharField(max_length=255,null=False)
    screenResolution =  models.CharField(max_length=255,null=False)
    ramSize =  models.CharField(max_length=255,null=False)
    ramType =  models.CharField(max_length=255,null=False)
    connections =  models.CharField(max_length=255,null=False)
    interfaces =  models.CharField(max_length=255,null=False)
    battery =  models.CharField(max_length=255,null=False)
    os =  models.CharField(max_length=255,null=False)
    speaker =  models.CharField(max_length=255,null=False)
    

    CategoryLaptop = models.ForeignKey(CategoryLaptop, default = None, on_delete = models.CASCADE)
    # Publisher = models.ForeignKey(Publisher, default = None, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.name}({self.manufacturer_date})"
# class BookAuthor (models.Model):
#     id  = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255,null=False)
#     bio = models.CharField(max_length=255,null=False)
#     def __str__(self):
#         return f"{self.name}({self.bio})"
# class Book_Author (models.Model):
#     id  = models.AutoField(primary_key=True)
#     Book = models.ForeignKey(Book, default = None, on_delete = models.CASCADE)
#     Author = models.ForeignKey(BookAuthor, default = None, on_delete = models.CASCADE)
#     def __str__(self):
#         return f"{self.Book}({self.Author})"
class ItemLaptop(models.Model):
    id  = models.AutoField(primary_key=True)
    Laptop = models.ForeignKey(Laptop, default = None, on_delete = models.CASCADE)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    promoText = models.CharField(max_length=255,null=False)
    description = models.CharField(max_length=255,null=False)
    inventory = models.CharField(max_length=255,null=False)
    is_for_sale = models.BooleanField(default=True,null=False)
    def __str__(self):
        return f"{self.Laptop}"
