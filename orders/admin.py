from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    list_display = ("diner", "restaurant", "status", "scheduled_datetime")
    list_filter = ("scheduled_datetime", "restaurant", "diner", "status")
    readonly_fields = ("cancelled_by", )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
