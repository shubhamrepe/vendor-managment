from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class YourSerializer(serializers.Serializer):
    order_date = serializers.DateTimeField(format='%d/%m/%Y --:--')
    delivery_date = serializers.DateTimeField(format='%d/%m/%Y --:--')
