from django.contrib import admin
from .models import Product, ProductVariation, Unit, Size, Color, Comment


admin.site.register(Unit)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductVariation)
admin.site.register(Comment)
