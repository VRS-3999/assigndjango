from django.db import models
# importing validationerror in below line
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

SHIP_MODE_CHOICES = (
            ('Regular Air', 'Regular Air'),
            ('Delivery Truck', 'Delivery Truck'),
            ('Express Air', 'Express Air')
    )

class Order(models.Model):
    order_id = models.CharField(max_length=191,null=False,blank=False)
    order_qty = models.CharField(max_length=191,null=False,blank=False)
    order_sales = models.FloatField(null=False,blank=False)
    order_ship_mode = models.CharField(max_length=50,choices=SHIP_MODE_CHOICES,blank=False, null=False)
    order_profit = models.FloatField(null=False,blank=False)
    order_unit_price = models.FloatField(null=False,blank=False)
    order_date = models.DateField(null=True,blank=True)
    order_date_new = models.CharField(max_length=50,null=True,blank=True)
    order_customer_name = models.CharField(max_length=50,null=True,blank=True)
    order_customer_segment = models.CharField(max_length=50,null=True,blank=True)
    order_product_category = models.CharField(max_length=50,null=True,blank=True)

