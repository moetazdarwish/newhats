from django.contrib import admin

# Register your models here.
from customers.models import *

admin.site.register(BusinessCategory)
admin.site.register(BusinessUnit)
admin.site.register(CustomerProfile)
admin.site.register(FAQ)
admin.site.register(Inventory)
admin.site.register(InventoryImage)
admin.site.register(AppCategory)
admin.site.register(ServiceHoliday)
admin.site.register(SlotBooking)
admin.site.register(ClincDoctor)
admin.site.register(ClincSub)


class ServiceHolidayInline(admin.TabularInline):
    model = ServiceHoliday
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['service', 'business','category','price','duration','Description','photo']
    inlines = [ServiceHolidayInline]
admin.site.register(Appointment, AppointmentAdmin)

class InventoryInline(admin.TabularInline):
    model = Inventory
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class InvCategoryAdmin(admin.ModelAdmin):
    list_display = ['business', 'cate']
    inlines = [InventoryInline]
admin.site.register(InvCategory, InvCategoryAdmin)

class ClincDoctorInline(admin.TabularInline):
    model = ClincDoctor
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class ClincDaysAdmin(admin.ModelAdmin):
    list_display = ['business','sub','day_nm','day','day_cl','off']
    inlines = [ClincDoctorInline]
admin.site.register(ClincDays, ClincDaysAdmin)