
from django.contrib import admin


from book.models import Book, Book_Author, BookAuthor, CategoryBook, ItemBook, Publisher,ImageBook

# Register your models here.
#Book
class BookAdmin(admin.ModelAdmin):
    # biểu diễn ra dạng bạng trên trang admin
    list_display = ("title","summary","publication_date","num_of_pages","language","dimesions","weight","edition","CategoryBook","Publisher")
    # thanh search
    search_fields = ["title"] 
    # tìm theo tag
    list_filter = ["CategoryBook"]
#đưa bảng lên trang admin
admin.site.register(Book,BookAdmin)

#Publisher
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name","address") 
    search_fields = ["name"] 
    list_filter = ["address"]
admin.site.register(Publisher,PublisherAdmin)
#CategoryBook
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ("type",) 
    search_fields = ["type"] 
admin.site.register(CategoryBook,CategoryBookAdmin)
#BookAuthor
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ("name","bio")
    search_fields = ["name"]
    list_filter = ["bio"]
admin.site.register(BookAuthor,BookAuthorAdmin)
#Book_Author
class Book_AuthorAdmin(admin.ModelAdmin):
    list_display = ("Book","Author")
    search_fields = ["Book","Author"]
admin.site.register(Book_Author,Book_AuthorAdmin)
#ImageBook
class ImageBookAdmin(admin.ModelAdmin):
    list_display = ("src","id")
    search_fields = ["src"]
admin.site.register(ImageBook,ImageBookAdmin)
#ItemBook
class ItemBookAdmin (admin.ModelAdmin):
    list_display = ("Book","price","discount","is_for_sale")
    search_fields = ["Book"]
admin.site.register(ItemBook,ItemBookAdmin)