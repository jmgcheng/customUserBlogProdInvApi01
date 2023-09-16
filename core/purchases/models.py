from django.db import models
from products.models import ProductVariation


class Purchase(models.Model):
    code = models.CharField(max_length=30, unique=True, blank=False, null=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.code


class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=False, null=True, related_name="purchase_detail")
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, related_name="product_variation")
    quantity_purchased = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f"PurchaseDetail #{self.id}"
    