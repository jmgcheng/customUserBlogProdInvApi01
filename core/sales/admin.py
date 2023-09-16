from django.contrib import admin
from .models import Sale, SaleDetail


class SaleAdmin(admin.ModelAdmin):
    list_display = ("code", "date")


class SaleDetailAdmin(admin.ModelAdmin):
    list_display = ("sale", "product_variation", "quantity_released")


admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleDetail, SaleDetailAdmin)
