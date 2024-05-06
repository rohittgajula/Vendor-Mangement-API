from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class STATUS_CHOICES(models.TextChoices):
  PENDING = 'pending'
  COMPLEATED = 'compleated'
  CANCELED = 'canceled'


class Vendor(models.Model):
  name = models.CharField(max_length=150)
  contact_details = models.TextField()
  address = models.TextField()
  vendor_code = models.CharField(max_length=30, unique=True)
  on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
  quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
  average_response_time = models.FloatField(validators=[MinValueValidator(0.0)])
  fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

  def __str__(self):
    return self.name
  

class PurchaseOrder(models.Model):
  po_number = models.CharField(max_length=100, unique=True)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  order_date = models.DateTimeField(auto_now_add=True)
  delivery_date = models.DateTimeField(auto_now=True)
  items = models.JSONField(null=True, blank=True)
  quantity = models.IntegerField()
  status = models.CharField(max_length=50, choices=STATUS_CHOICES.choices, default="PENDING")
  quality_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], null=True)
  issue_date = models.DateTimeField()
  acknowledgment_date = models.DateTimeField(null=True)

  def __str__(self):
    return f"PO {str(self.po_number)}"


class HistoricalPerformance(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
  quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
  average_response_time = models.FloatField(validators=[MinValueValidator(0.0)])
  fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

  def __str__(self):
    return f"{self.vendor.name} - {self.date}"
  
