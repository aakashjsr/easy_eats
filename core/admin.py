from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import Tag, Location, FoodCategory

admin.site.unregister(Group)

admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(FoodCategory)


admin.site.site_header = 'EasyEats Administration'
