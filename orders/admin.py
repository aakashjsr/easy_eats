from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("member", "restaurant", "status", "scheduled_datetime")
    list_filter = ("scheduled_datetime", "restaurant", "member", "status")


admin.site.register(Order, OrderAdmin)
