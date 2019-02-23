from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    list_display = ("member", "restaurant", "status", "scheduled_datetime")
    list_filter = ("scheduled_datetime", "restaurant", "member", "status")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
