from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ("order_id", "cancelled_by")
    inlines = [OrderItemInline]
    list_display = ("diner", "order_id", "restaurant", "restaurant_id", "status", "created", "scheduled_datetime", "completed_datetime")
    list_filter = ("scheduled_datetime", "restaurant", "diner", "status", "created")
    search_fields = ("diner__user__first_name", "order_id")



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
