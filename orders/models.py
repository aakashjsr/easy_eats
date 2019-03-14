from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import Diner, User
from model_utils.models import TimeStampedModel
from core.utils import generate_alphanumeric_id
from restaurants.models import Restaurant, FoodItem, FoodItemAddon


class Order(TimeStampedModel):
    ACTIVE = "ACTIVE"
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    ON_TIME = "On Time"
    LATE_BY_5 = "Late by 5 mins"
    LATE_BY_10 = "Late by more than 10 mins"
    EARLY_BY_10 = "Early by more than 10 mins"
    EARLY_BY_5 = "Early by 5 mins"
    DINE_IN = "Dine-In"
    TAKEAWAY = "Takeaway"

    RESTAURANT_RATING_CHOICES = [
        (0, EARLY_BY_5),
        (1, EARLY_BY_10),
        (2, ON_TIME),
        (3, LATE_BY_5),
        (4, LATE_BY_10),
    ]

    order_id = models.CharField(null=True, blank=True, max_length=6, unique=True, db_index=True)
    diner = models.ForeignKey(Diner, related_name="diners", on_delete=models.CASCADE)
    cancelled_by = models.ForeignKey(
        User, related_name="orders_cancelled", on_delete=models.CASCADE, null=True, blank=True
    )
    restaurant = models.ForeignKey(
        Restaurant, related_name="orders", on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=[
            (ACTIVE, ACTIVE),
            (BOOKED, BOOKED),
            (COMPLETED, COMPLETED),
            (CANCELLED, CANCELLED),
        ],
        default=BOOKED,
    )
    comment = models.TextField(blank=True)
    order_type = models.CharField(max_length=50, choices=[
        (TAKEAWAY, TAKEAWAY), (DINE_IN, DINE_IN)
    ], default=TAKEAWAY)
    seats = models.PositiveIntegerField(default=0)
    food_items = models.ManyToManyField(FoodItem, through="OrderItem", related_name="orders")
    scheduled_datetime = models.DateTimeField()
    completed_datetime = models.DateTimeField(null=True, blank=True)
    cancellation_charge = models.DecimalField(
        default=0, max_digits=10, decimal_places=2
    )
    sub_total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    points_earned = models.PositiveIntegerField(default=0)
    user_rating = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    restaurant_rating = models.SmallIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    restaurant_timing_rating = models.SmallIntegerField(
        null=True, blank=True, choices=RESTAURANT_RATING_CHOICES
    )
    user_review = models.TextField(null=True, blank=True, max_length=280)
    restaurant_review = models.TextField(blank=True, max_length=280)
    diner_delay = models.PositiveIntegerField(
        null=True, blank=True, validators=[MinValueValidator(1)]
    )
    is_repeat_order = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}".format(self.diner, self.restaurant, self.order_type)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.order_id = generate_alphanumeric_id()
        super().save(*args, **kwargs)


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    comment = models.TextField(blank=True)
    addons = models.ManyToManyField(FoodItemAddon, related_name="order_items", blank=True)
