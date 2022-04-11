
from django.contrib import admin


from clothes.models import Clothes, CategoryClothes, ItemClothes

# Register your models here.
#Book
class ClothesAdmin(admin.ModelAdmin):
    # biểu diễn ra dạng bạng trên trang admin
    list_display = ("name","brand","color","manufacturerDate","material","department","size","sizeCountry","washingType","weight","fitType","closureType","dimensions","countryOrigin","CategoryClothes")
    # thanh search
    search_fields = ["name"] 
    # tìm theo tag
    list_filter = ["CategoryClothes"]
#đưa bảng lên trang admin
admin.site.register(Clothes,ClothesAdmin)

#CategoryBook
class CategoryClothesAdmin(admin.ModelAdmin):
    list_display = ("type",) 
    search_fields = ["type"] 
admin.site.register(CategoryClothes,CategoryClothesAdmin)

#ItemBook
class ItemClothesAdmin (admin.ModelAdmin):
    list_display = ("Clothes","price","discount","isForSale")
    search_fields = ["Clothes"]
admin.site.register(ItemClothes,ItemClothesAdmin)