from pyexpat import model
from django.db import models

# Create your models here.
class Publisher (models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    address = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.name}({self.address})"
class CategoryBook (models.Model):
    id  = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255,null=False)
    def __str__(self):
        return f"{self.type}"
class Book (models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,null=False)
    summary = models.CharField(max_length=255,null=False)
    publication_date = models.DateField(null=False)
    num_of_pages = models.IntegerField(null=True)
    language = models.CharField(max_length=255,null=False)
    dimesions = models.CharField(max_length=255,null=False)
    weight = models.FloatField(null=True)
    edition =  models.CharField(max_length=255,null=False)
    CategoryBook = models.ForeignKey(CategoryBook, default = None, on_delete = models.CASCADE)
    Publisher = models.ForeignKey(Publisher, default = None, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.title}({self.publication_date})"
