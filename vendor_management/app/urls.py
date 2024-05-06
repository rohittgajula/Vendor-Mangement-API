from django.urls import path
from .views import VendorListCreateAPIView, VendorRetriveUpdateDeleteAPIView, PurchaseOrderListCreateAPIView, PurchaseOrderRetriveUpdateDeleteAPIView, VendorPerformanceView


urlpatterns = [
  # Vendor
  path("vendors/", VendorListCreateAPIView.as_view(), name="create-get-vendor"),
  path("vendors/<str:vendor_id>/", VendorRetriveUpdateDeleteAPIView.as_view(), name="retrive-update-delete-vendor"),

  #Purchase Order
  path("purchase_orders/", PurchaseOrderListCreateAPIView.as_view(), name="create-get-purchase_order"),
  path("purchase_orders/<str:po_id>/", PurchaseOrderRetriveUpdateDeleteAPIView.as_view(), name="retrive-update-delete-purchase_order"),

  # Vendor performance
  path("vendors/<str:vendor_id>/performance/", VendorPerformanceView.as_view(), name="vendor-performance"),
]