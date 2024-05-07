from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg, F
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    total_orders = vendor.purchase_orders.filter(status='completed').count()
    on_time_delivery_rate = vendor.purchase_orders.filter(status='completed', 
        delivery_date__lte=F('acknowledgment_date')).count() / total_orders * 100 if total_orders > 0 else 0
    quality_rating_avg = vendor.purchase_orders.filter(status='completed').aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    average_response_time = vendor.purchase_orders.filter(status='completed', acknowledgment_date__isnull=False).aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg'] or 0
    fulfillment_rate = vendor.purchase_orders.filter(status='completed').count() / vendor.purchase_orders.count() * 100 if vendor.purchase_orders.count() > 0 else 0

    performance_metrics = {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': average_response_time,
        'fulfillment_rate': fulfillment_rate
    }

    return Response(performance_metrics)
