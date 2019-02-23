from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User, RestaurantOwner, RestaurantStaff, Member


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
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
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )

    fieldsets = (
        ('Login Info', {'fields': ('password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        ('Admin Info', {'fields': ('is_staff', 'is_superuser')}),
    )


class RestaurantOwnerAdmin(admin.ModelAdmin):
    model = RestaurantOwner

    search_fields = ("user__email", "user__first_name")


class RestaurantStaffAdmin(admin.ModelAdmin):
    model = RestaurantStaff
    search_fields = ("user__email", "user__first_name")


class MemberAdmin(admin.ModelAdmin):
    model = RestaurantStaff
    search_fields = ("user__email", "user__first_name")


admin.site.register(User, MyUserAdmin)
admin.site.register(RestaurantOwner, RestaurantOwnerAdmin)
admin.site.register(RestaurantStaff, RestaurantStaffAdmin)
admin.site.register(Member, MemberAdmin)
