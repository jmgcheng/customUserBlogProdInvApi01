from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from html_sanitizer.django import get_sanitizer


class Unit(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
        

class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=30, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    excerpt = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image_url = models.CharField(max_length=2083, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        sanitizer = get_sanitizer()
        self.excerpt = sanitizer.sanitize(self.excerpt)
        self.description = sanitizer.sanitize(self.description)

        super().save(*args, **kwargs)      


class ProductVariation(models.Model):
    code = models.CharField(max_length=30, unique=True, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=False, null=True, related_name="product")
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    excerpt = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=False, null=True, related_name="unit")
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, blank=True, null=True, related_name="size")
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, related_name="color")
    image_url = models.CharField(max_length=2083, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-variation-detail', kwargs={'pk': self.pk})

    def current_inventory_quantity(self):
        total_purchased = self.product_variation.all().aggregate(Sum('quantity_purchased'))['quantity_purchased__sum'] or 0
        total_sold = self.sale_product_variation.all().aggregate(Sum('quantity_released'))['quantity_released__sum'] or 0
        current_quantity = total_purchased - total_sold
        
        return current_quantity

    def save(self, *args, **kwargs):
        sanitizer = get_sanitizer()
        self.excerpt = sanitizer.sanitize(self.excerpt)
        self.description = sanitizer.sanitize(self.description)

        super().save(*args, **kwargs)    


class Comment(models.Model):
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="user")
    content = models.TextField(max_length=400, blank=False, null=False)
    date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        sanitizer = get_sanitizer()
        self.content = sanitizer.sanitize(self.content)

        super().save(*args, **kwargs)  
