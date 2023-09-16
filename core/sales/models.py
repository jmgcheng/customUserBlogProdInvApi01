from django.db import models
from products.models import ProductVariation


class Sale(models.Model):
    code = models.CharField(max_length=30, unique=True, blank=False, null=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.code


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, blank=False, null=True, related_name="sale_detail")
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, related_name="sale_product_variation")
    quantity_released = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f"SaleDetail #{self.id}"
    