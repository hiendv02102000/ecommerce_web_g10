
from django.contrib import admin


from shoes.models import Shoes,CategoryShoes,ImageShoes,ItemShoes

# Register your models here.
#Shoes
class ShoesAdmin(admin.ModelAdmin):
    # biểu diễn ra dạng bạng trên trang admin
    list_display = ("name","size","sizeCountry","brand","color","weight","manufactureDate","countryOrigin","department","upperMaterial","sideMaterial","liningMaterial","dimensions","CategoryShoes")
    # thanh search
    search_fields = ["name"] 
    # tìm theo tag
    list_filter = ["CategoryShoes"]
#đưa bảng lên trang admin
admin.site.register(Shoes,ShoesAdmin)

#CategoryShoes
class CategoryShoesAdmin(admin.ModelAdmin):
    list_display = ("type",) 
    search_fields = ["type"] 
admin.site.register(CategoryShoes,CategoryShoesAdmin)

#ImageShoes
class ImageShoesAdmin(admin.ModelAdmin):
    list_display = ("src",)
    search_fields = ["src"]
admin.site.register(ImageShoes,ImageShoesAdmin)

#ItemShoes
class ItemShoesAdmin (admin.ModelAdmin):
    list_display = ("Shoes","price","discount","is_for_sale")
    search_fields = ["Shoes"]
admin.site.register(ItemShoes,ItemShoesAdmin)