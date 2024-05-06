from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, action

from .models import Vendor, HistoricalPerformance, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

from drf_yasg.utils import swagger_auto_schema
from django.db.models import Avg, Count

from rest_framework.permissions import IsAuthenticated

class VendorListCreateAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response({
    'vendors':serializer.data
  }, status.HTTP_200_OK)
  
  @action(detail=False, methods=['POST'])
  @swagger_auto_schema(request_body=VendorSerializer)
  def post(self, request):
    data = request.data
    serializer = VendorSerializer(data=data)
    if serializer.is_valid():
      vendor = Vendor.objects.create(**data)
      ven = VendorSerializer(vendor, many=False)
      return Response({
        'details':ven.data
      }, status.HTTP_201_CREATED)
    return Response(serializer.errors)
  

class VendorRetriveUpdateDeleteAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if vendor:
      serializer = VendorSerializer(vendor, many=False)
      return Response({
        'vendor':serializer.data
      }, status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  @action(detail=False, methods=['PUT'])
  @swagger_auto_schema(request_body=VendorSerializer)
  def put(self, request, vendor_id):
    data = request.data
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if vendor:
      serializer = VendorSerializer(vendor, data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          'details':serializer.data
        }, status.HTTP_202_ACCEPTED)
      return Response(serializer.errors)
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  def delete(self, request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if vendor:
      vendor.delete()
      return Response("Vendor deleted sucessfully.")
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  
class PurchaseOrderListCreateAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    purchase_order = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_order, many=True)
    return Response({
      'details':serializer.data
    }, status.HTTP_200_OK)
  
  @action(detail=False, methods=['POST'])
  @swagger_auto_schema(request_body=PurchaseOrderSerializer)
  def post(self, request):
    data = request.data
    serializer = PurchaseOrderSerializer(data=data)
    if serializer.is_valid():
      vendor_id = data.get('vendor')
      try:
        vendor_instance = Vendor.objects.get(id=vendor_id)
      except Vendor.DoesNotExist:
        return Response({
          'error':"Vendor does not exists."
        }, status.HTTP_400_BAD_REQUEST)
      print(vendor_instance)
      data['vendor'] = vendor_instance
      purchaseOrder = PurchaseOrder.objects.create(**data)
      order_serializer = PurchaseOrderSerializer(purchaseOrder, many=False)
      return Response({
        'details':order_serializer.data
      }, status.HTTP_200_OK)
    return Response(serializer.errors)
  

class PurchaseOrderRetriveUpdateDeleteAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    serializer = PurchaseOrderSerializer(purchase_order, many=False)
    return Response({
      'details':serializer.data
    }, status.HTTP_200_OK)
  
  @action(detail=False, methods=['PUT'])
  @swagger_auto_schema(request_body=PurchaseOrderSerializer)
  def put(self, request, po_id):
    data = request.data
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    if purchase_order:
      serializer = PurchaseOrderSerializer(purchase_order, data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          'details':serializer.data
        }, status.HTTP_202_ACCEPTED)
      return Response(serializer.errors)
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  def delete(self, request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    if purchase_order:
      purchase_order.delete()
      return Response("Purchase Order deleted sucessfully.")
    return Response(status=status.HTTP_404_NOT_FOUND)
  

class VendorPerformanceView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, vendor_id):
      vendor = get_object_or_404(Vendor, pk=vendor_id)
      performance_metrics = {
          'on_time_delivery_rate': vendor.on_time_delivery_rate,
          'quality_rating_avg': vendor.quality_rating_avg,
          'average_response_time': vendor.average_response_time,
          'fulfillment_rate': vendor.fulfillment_rate
      }
      return Response(performance_metrics)
  
