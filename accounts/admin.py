from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User, RestaurantOwner, RestaurantStaff, Diner


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "mobile")
        field_classes = {'username': "email"}


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'username': "email"}


class MyUserAdmin(UserAdmin):
    search_fields = ("first_name", "email")
    add_form = MyUserCreateForm
    ordering = ("email",)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'mobile')}),
    )

    fieldsets = (
        ('Login Info', {'fields': ('password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        ('Admin Info', {'fields': ('is_staff', 'is_superuser')}),
    )


class RestaurantOwnerAdmin(admin.ModelAdmin):
    model = RestaurantOwner
    list_display = ("get_first_name", "get_email", "get_restaurants", "get_mobile", "id")

    def get_email(self, instance):
        return instance.user.email

    def get_mobile(self, instance):
        return instance.user.mobile

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_restaurants(self, instance):
        return list(instance.restaurants.values_list("name", flat=True))

    get_email.short_description = 'Email'
    get_first_name.short_description = 'First Name'
    get_mobile.short_description = 'Phone'
    get_restaurants.short_description = 'Restaurants'

    search_fields = ("user__email", "user__first_name", "user__mobile")


class RestaurantStaffAdmin(admin.ModelAdmin):
    model = RestaurantStaff
    list_display = ("get_first_name", "get_email", "get_restaurants", "get_mobile", "id")

    def get_email(self, instance):
        return instance.user.email

    def get_mobile(self, instance):
        return instance.user.mobile

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_restaurants(self, instance):
        return list(instance.restaurants.values_list("name", flat=True))

    get_email.short_description = 'Email'
    get_first_name.short_description = 'First Name'
    get_mobile.short_description = 'Phone'
    get_restaurants.short_description = 'Restaurants'

    search_fields = ("user__email", "user__first_name", "user__mobile")


class DinerAdmin(admin.ModelAdmin):

    model = Diner
    list_filter = ("created", )
    list_display = ("created", "get_first_name", "get_email", "get_mobile", "id")

    def get_email(self, instance):
        return instance.user.email

    def get_mobile(self, instance):
        return instance.user.mobile

    def get_first_name(self, instance):
        return instance.user.first_name

    get_email.short_description = 'Email'
    get_first_name.short_description = 'First Name'
    get_mobile.short_description = 'Phone'

    search_fields = ("user__email", "user__first_name", "user__mobile")


admin.site.register(User, MyUserAdmin)
admin.site.register(RestaurantOwner, RestaurantOwnerAdmin)
admin.site.register(RestaurantStaff, RestaurantStaffAdmin)
admin.site.register(Diner, DinerAdmin)
