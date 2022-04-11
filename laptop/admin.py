
from django.contrib import admin


# from laptop.models import Book, Book_Author, BookAuthor, CategoryBook, ItemBook, Publisher
from laptop.models import Laptop, CategoryLaptop, ItemLaptop

# Register your models here.
#Book
class LaptopAdmin(admin.ModelAdmin):
    # biểu diễn ra dạng bạng trên trang admin
    list_display = ("name","manufacturer_date","weight","color","warranty","dimensions","countryOrigin","cpu","gpu","storageSize","storageType", "screenSize", "screenResolution", "ramSize", "ramType", "connections", "interfaces", "battery", "os", "speaker")
    # thanh search
    search_fields = ["name"] 
    # tìm theo tag
    list_filter = ["CategoryLaptop"]
#đưa bảng lên trang admin
admin.site.register(Laptop,LaptopAdmin)

#Publisher
# class PublisherAdmin(admin.ModelAdmin):
#     list_display = ("name","address") 
#     search_fields = ["name"] 
#     list_filter = ["address"]
# admin.site.register(Publisher,PublisherAdmin)
#CategoryBook
class CategoryLaptopAdmin(admin.ModelAdmin):
    list_display = ("type",) 
    search_fields = ["type"] 
admin.site.register(CategoryLaptop, CategoryLaptopAdmin)
#BookAuthor
# class BookAuthorAdmin(admin.ModelAdmin):
#     list_display = ("name","bio")
#     search_fields = ["name"]
#     list_filter = ["bio"]
# admin.site.register(BookAuthor,BookAuthorAdmin)
# #Book_Author
# class Book_AuthorAdmin(admin.ModelAdmin):
#     list_display = ("Book","Author")
#     search_fields = ["Book","Author"]
# admin.site.register(Book_Author,Book_AuthorAdmin)
#ItemBook
class ItemlaptopAdmin (admin.ModelAdmin):
    list_display = ("Laptop","price","discount","promoText", "description", "inventory","is_for_sale")
    search_fields = ["Laptop"]
admin.site.register(ItemLaptop,ItemlaptopAdmin)
