from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from purchases.models import Purchase, PurchaseDetail
from sales.models import Sale, SaleDetail
from products.models import Product, ProductVariation
from .serializers import PurchaseSerializer, PurchaseDetailSerializer, SaleSerializer, SaleDetailSerializer, ProductVariationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PurchaseListCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer  # Use the PurchaseSerializer for this view
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]    

    def perform_create(self, serializer):
        # Override perform_create to handle saving related PurchaseDetail objects
        purchase = serializer.save()
        # purchase_details_data = self.request.data.get('purchase_detail', [])
        # for detail_data in purchase_details_data:
        #     PurchaseDetail.objects.create(purchase=purchase, **detail_data)

    def get_serializer_context(self):
        # Pass the request data to the serializer context
        context = super().get_serializer_context()
        context.update({'request_data': self.request.data})
        return context

    def get_serializer(self, *args, **kwargs):
        # Use different serializers for POST and GET requests
        if self.request.method == 'POST':
            return PurchaseSerializer(*args, **kwargs)
        # return PurchaseDetailSerializer(*args, **kwargs)
        return PurchaseSerializer(*args, **kwargs)



class PurchaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]    

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     # You can customize the response message and status code here
    #     data = {
    #         "message": f"Purchase with id {instance.id} was updated successfully.",
    #         "status": status.HTTP_200_OK,
    #     }
    #     return Response(data, status=status.HTTP_200_OK)

    # def perform_destroy(self, instance):
    #     instance.delete()
    #     # You can customize the response message and status code here
    #     data = {
    #         "message": f"Purchase with id {instance.id} was deleted successfully.",
    #         "status": status.HTTP_204_NO_CONTENT,
    #     }
    #     return Response(data, status=status.HTTP_204_NO_CONTENT)





class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer  # Use the SaleSerializer for this view
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]    

    def perform_create(self, serializer):
        sale = serializer.save()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request_data': self.request.data})
        return context

    def get_serializer(self, *args, **kwargs):
        return SaleSerializer(*args, **kwargs)


class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]    



class ProductVariationListCreateView(generics.ListCreateAPIView):
    queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]



class ProductVariationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]
