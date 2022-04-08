
from django.contrib import admin


from book.models import Book, CategoryBook, Publisher

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","summary","publication_date","num_of_pages","language","dimesions","weight","edition","CategoryBook","Publisher")
    search_fields = ["title"] 
    list_filter = ["title"]
admin.site.register(Book,BookAdmin)

admin.site.register(Publisher)
admin.site.register(CategoryBook)