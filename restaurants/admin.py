from django.contrib import admin
from django.utils.html import mark_safe
from restaurants.models import FoodItem, Restaurant, FoodItemAddon


class FoodItemAddonInline(admin.TabularInline):
    model = FoodItemAddon


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "get_category", "get_tags")
    inlines = [FoodItemAddonInline]
    model = FoodItem
    list_filter = ("restaurant__name", "category", )
    search_fields = ("name", "restaurant__name")

    def get_tags(self, instance):
        return list(instance.tags.values_list("name", flat=True))

    def get_category(self, instance):
        return instance.category

    get_category.short_description = "Cuisine"
    get_category.admin_order_field = "category"
    get_tags.short_description = "Tags"


class FoodItemInline(admin.TabularInline):
    model = FoodItem


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    inlines = [FoodItemInline]
    list_display = (
        "id",
        "name",
        "get_total_orders",
        "created",
        "dineout_online",
        "takeaway_online",
        "search_position",
        "get_contact_email",
        "get_contact_mobile",
    )

    def get_contact_email(self, instance):
        return instance.owner.user.email

    def get_contact_mobile(self, instance):
        return instance.owner.user.mobile

    def get_total_orders(self, instance):
        return instance.orders.count()

    get_contact_email.short_description = "Contact Email"
    get_contact_mobile.short_description = "Contact Phone"
    get_total_orders.short_description = "Total Orders"
    get_total_orders.admin_order_field = "name"

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

