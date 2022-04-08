
from django.contrib import admin


from book.models import Book, CategoryBook, Publisher

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # biểu diễn ra dạng bạng trên trang admin
    list_display = ("title","summary","publication_date","num_of_pages","language","dimesions","weight","edition","CategoryBook","Publisher")
    # thanh search
    search_fields = ["title"] 
    # tìm theo tag
    list_filter = ["CategoryBook"]
#đưa bảng lên trang admin
admin.site.register(Book,BookAdmin)

admin.site.register(Publisher)
admin.site.register(CategoryBook)