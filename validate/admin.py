from django.contrib import admin
from .models import *
#https://devhints.io/datetime

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    def order_dates(self,obj):
        try:
            return obj.order_date.strftime("%d-%b-%Y")
        except:
            return "Value is not Inserted"
    list_display =['order_id','order_qty','order_sales','order_ship_mode','order_profit','order_unit_price','order_dates','order_date_new','order_customer_name','order_customer_segment','order_product_category']
admin.site.register(Order, OrderAdmin)
