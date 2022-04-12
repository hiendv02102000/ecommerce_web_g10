from django.contrib import admin

# Register your models here.
from mobile_phone.models import MobilePhone,ItemMobilePhone,CategoryMobilePhone
class MobilePhoneAdmin(admin.ModelAdmin):
    # biểu diễn ra dạng bạng trên trang admin
    list_display = ("name","manufacturer_date","weight","color","warranty","dimensions","countryOrigin","cpu","gpu","storageSize", "screenSize", "screenResolution", "ramSize", "ramType", "connections", "interfaces", "battery", "os", "speaker","frontCamera","rearCamera")
    # thanh search
    search_fields = ["name"] 
    # tìm theo tag
    list_filter = ["CategoryMobilePhone"]
#đưa bảng lên trang admin
admin.site.register(MobilePhone,MobilePhoneAdmin)


class CategoryMobilePhoneAdmin(admin.ModelAdmin):
    list_display = ("type",) 
    search_fields = ["type"] 
admin.site.register(CategoryMobilePhone, CategoryMobilePhoneAdmin)

class ItemMobilePhoneAdmin (admin.ModelAdmin):
    list_display = ("mobilePhone","price","discount","promoText", "description", "inventory","is_for_sale")
    search_fields = ["mobilePhone"]
admin.site.register(ItemMobilePhone,ItemMobilePhoneAdmin)
