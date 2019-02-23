from django.contrib import admin

from restaurants.models import FoodItem, Restaurant


class FoodItemAdmin(admin.ModelAdmin):
    model = FoodItem
    list_filter = ("restaurant__name",)
    search_fields = ("name", "restaurant__name")


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = (
        "name",
        "owner",
        "dineout_online",
        "takeaway_online",
        "search_position",
    )
    search_fields = ("name",)


admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
