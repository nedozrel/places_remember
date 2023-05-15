from django.db import models
# pylint: disable=imported-auth-user
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    Base model providing timestamp fields for created and updated times.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Place(BaseModel):
    """
    Model representing a place with a title, description,
    geographic coordinates, and associated user.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'
