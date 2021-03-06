from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from model_utils.models import TimeStampedModel
from accounts.models import RestaurantStaff, RestaurantOwner
from core.models import FoodCategory, Tag, Location


class Restaurant(TimeStampedModel):
    """
    Restaurant model
    """

    SELF_SERVICE = "Self Service"
    FULL_SERIVCE = "Full Service"

    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="restaurants", null=True, blank=True)
    type = models.SmallIntegerField(
        choices=[(0, SELF_SERVICE), (1, FULL_SERIVCE)],
        default=1,
    )
    address = models.TextField()
    phone = models.CharField(max_length=20)
    staff = models.ForeignKey(RestaurantStaff, on_delete=models.CASCADE, related_name="restaurants")
    owner = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE, related_name="restaurants")
    franchise_name = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255)
    bank_acc_name = models.CharField(max_length=255)
    bank_acc_number = models.CharField(max_length=255)
    transaction_fee_rate = models.DecimalField("Transaction fee rate (%)",
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
    )
    sales_service_tax = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
    )
    service_charge_rate = models.DecimalField("Service charge rate (%)",
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
    )
    has_dine_in_service_charge = models.BooleanField(default=False)
    has_takeaway_service_charge = models.BooleanField(default=False)
    rating = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    dineout_online = models.BooleanField(default=False)
    takeaway_online = models.BooleanField(default=False)
    search_position = models.PositiveIntegerField(
        null=True, blank=True, validators=[MinValueValidator(1)]
    )
    seats = models.PositiveIntegerField(default=0)
    display_image = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    cost_index = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(4), MinValueValidator(1)]
    )

    open_on_monday = models.BooleanField(default=True)
    monday_opening_time = models.TimeField(default="00:00")
    monday_closing_time = models.TimeField(default="00:00")

    open_on_tuesday = models.BooleanField(default=True)
    tuesday_opening_time = models.TimeField(default="00:00")
    tuesday_closing_time = models.TimeField(default="00:00")

    open_on_wednesday = models.BooleanField(default=True)
    wednesday_opening_time = models.TimeField(default="00:00")
    wednesday_closing_time = models.TimeField(default="00:00")

    open_on_thursday = models.BooleanField(default=True)
    thursday_opening_time = models.TimeField(default="00:00")
    thursday_closing_time = models.TimeField(default="00:00")

    open_on_friday = models.BooleanField(default=True)
    friday_opening_time = models.TimeField(default="00:00")
    friday_closing_time = models.TimeField(default="00:00")

    open_on_saturday = models.BooleanField(default=True)
    saturday_opening_time = models.TimeField(default="00:00")
    saturday_closing_time = models.TimeField(default="00:00")

    open_on_sunday = models.BooleanField(default=True)
    sunday_opening_time = models.TimeField(default="00:00")
    sunday_closing_time = models.TimeField(default="00:00")

    scheduled_closing_dates = models.CharField(max_length=2000, null=True, blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        data = super().save(*args, **kwargs)
        if Restaurant.objects.filter(search_position=self.search_position).count() > 1:
            Restaurant.objects.filter(
                search_position__gte=self.search_position
            ).exclude(id=self.id).update(search_position=models.F("search_position") + 1)
        return data


class FoodItem(TimeStampedModel):
    """
    Stores food items per restaurant
    """

    restaurant = models.ForeignKey(
        Restaurant, related_name="food_items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        FoodCategory, related_name="food_items", on_delete=models.CASCADE
    )
    image = models.ImageField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="food_items", db_index=True)
    has_dairy = models.BooleanField(default=False)
    has_nuts = models.BooleanField(default=False)
    is_veg = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_halal = models.BooleanField(default=False)
    is_non_halal = models.BooleanField(default=False)
    unlimited_addons_required = models.BooleanField(default=False)
    limited_addons_required = models.BooleanField(default=False)
    single_addons_required = models.BooleanField(default=False)
    max_limited_addons = models.PositiveIntegerField(default=10)

    def __str__(self):
        return "{} - {}".format(self.name, self.restaurant)


class FoodItemAddon(TimeStampedModel):
    """
    Add ons for food items
    """
    UNLIMITED = "Unlimited"
    LIMITED = "Limited"
    SINGLE = "Single"

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=[
        (UNLIMITED, UNLIMITED), (LIMITED, LIMITED), (SINGLE, SINGLE)
    ], default=UNLIMITED)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="addons")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1024, null=True, blank=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.food_item.name, self.name)
