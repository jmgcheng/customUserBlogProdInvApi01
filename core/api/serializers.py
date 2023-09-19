from rest_framework import serializers
from purchases.models import Purchase, PurchaseDetail
from sales.models import Sale, SaleDetail
from products.models import Color, Unit, Size, Product, ProductVariation


class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        fields = ('product_variation', 'quantity_purchased')


class PurchaseSerializer(serializers.ModelSerializer):
    purchase_detail = PurchaseDetailSerializer(many=True)  # Serializer for the related PurchaseDetail objects

    class Meta:
        model = Purchase
        fields = ('code', 'purchase_detail')  # Include other fields from the Purchase model as needed

    def create(self, validated_data):
        # Extract and create PurchaseDetail instances
        purchase_detail_data = validated_data.pop('purchase_detail')
        purchase = Purchase.objects.create(**validated_data)
        for detail_data in purchase_detail_data:
            PurchaseDetail.objects.create(purchase=purchase, **detail_data)
        return purchase

    def update(self, instance, validated_data):
        purchase_detail_data = validated_data.pop('purchase_detail', [])
        
        # Update the fields of the Purchase instance
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        
        # Handle updates for related PurchaseDetail instances
        updated_purchase_details = []
        for detail_data in purchase_detail_data:
            product_variation = detail_data['product_variation']
            quantity_purchased = detail_data['quantity_purchased']
            
            # Check if the PurchaseDetail instance already exists
            purchase_detail, created = PurchaseDetail.objects.get_or_create(
                purchase=instance, product_variation=product_variation
            )
            
            # Update the quantity_purchased for the PurchaseDetail
            purchase_detail.quantity_purchased = quantity_purchased
            purchase_detail.save()
            
            updated_purchase_details.append(purchase_detail)
        
        # Remove any PurchaseDetail instances that were not updated
        instance.purchase_detail.exclude(pk__in=[pd.pk for pd in updated_purchase_details]).delete()
        
        return instance
    









class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = ('product_variation', 'quantity_released')    


class SaleSerializer(serializers.ModelSerializer):
    sale_detail = SaleDetailSerializer(many=True)  # Serializer for the related SaleDetail objects

    class Meta:
        model = Sale
        fields = ('code', 'sale_detail')  # Include other fields from the Purchase model as needed

    def create(self, validated_data):
        # Extract and create SaleDetail instances
        sale_detail_data = validated_data.pop('sale_detail')
        sale = Sale.objects.create(**validated_data)
        for detail_data in sale_detail_data:
            SaleDetail.objects.create(sale=sale, **detail_data)
        return sale

    def update(self, instance, validated_data):
        sale_detail_data = validated_data.pop('sale_detail', [])
        
        # Update the fields of the Sale instance
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        
        # Handle updates for related SaleDetail instances
        updated_sale_details = []
        for detail_data in sale_detail_data:
            product_variation = detail_data['product_variation']
            quantity_released = detail_data['quantity_released']
            
            # Check if the SaleDetail instance already exists
            sale_detail, created = SaleDetail.objects.get_or_create(
                sale=instance, product_variation=product_variation
            )
            
            # Update the quantity_released for the SaleDetail
            sale_detail.quantity_released = quantity_released
            sale_detail.save()
            
            updated_sale_details.append(sale_detail)
        
        # Remove any SaleDetail instances that were not updated
        instance.sale_detail.exclude(pk__in=[pd.pk for pd in updated_sale_details]).delete()
        
        return instance        





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class ProductVariationSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    unit = UnitSerializer()
    size = SizeSerializer()
    color = ColorSerializer()

    class Meta:
        model = ProductVariation
        fields = '__all__'
