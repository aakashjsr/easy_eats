from django.contrib import admin
from django.utils.html import mark_safe
from restaurants.models import FoodItem, Restaurant, FoodItemAddon


class FoodItemAddonInline(admin.TabularInline):
    model = FoodItemAddon


class FoodItemAdmin(admin.ModelAdmin):
    inlines = [FoodItemAddonInline]
    model = FoodItem
    list_filter = ("restaurant__name",)
    search_fields = ("name", "restaurant__name")


class FoodItemInline(admin.TabularInline):
    model = FoodItem


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    inlines = [FoodItemInline]
    list_display = (
        "name",
        "owner",
        "dineout_online",
        "takeaway_online",
        "search_position",
    )

    search_fields = ("name",)
    readonly_fields = ("preview_display_image", )

    def preview_display_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.display_image.url,
            width=obj.display_image.width,
            height=obj.display_image.height,
        )
        )


admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(FoodItemAddon)
