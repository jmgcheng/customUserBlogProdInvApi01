from django.contrib import admin
from .models import Purchase, PurchaseDetail


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("code", "date")


class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ("purchase", "product_variation", "quantity_purchased")


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseDetail, PurchaseDetailAdmin)
