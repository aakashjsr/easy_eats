from django.db import models
from model_utils.models import TimeStampedModel


class Tag(TimeStampedModel):
    """
    Model to store tags
    """

    name = models.CharField(max_length=30, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Location(TimeStampedModel):
    """
    Model to store locations
    """

    name = models.CharField(max_length=50, db_index=True)
    city = models.CharField(max_length=50, db_index=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.city)


class FoodCategory(TimeStampedModel):
    """
    Model to store food category
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Food Categories"
