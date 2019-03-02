from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from model_utils.models import TimeStampedModel
from accounts.object_managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Base User model
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    mobile = models.CharField(max_length=25, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):

        return "{} - {}".format(self.first_name, self.email)


class RestaurantOwner(TimeStampedModel):
    """
    Restaurant Owner
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.user.get_full_name(), self.user.email)


class RestaurantStaff(TimeStampedModel):
    """
    Restaurant Staff
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.user.get_full_name(), self.user.email)


class Diner(TimeStampedModel):
    """
    Member
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referred_by = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )
    loyalty_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.user.get_full_name(), self.user.email)
