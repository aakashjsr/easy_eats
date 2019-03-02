from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import Tag, Location, FoodCategory

admin.site.unregister(Group)


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("area", "town", "city", "postcode")

admin.site.register(Tag)
admin.site.register(Location, LocationAdmin)
admin.site.register(FoodCategory)


admin.site.site_header = 'EasyEats Administration'
