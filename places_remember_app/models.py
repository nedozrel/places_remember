from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        abstract = True


class Place(BaseModel):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # pylint: disable=too-few-public-methods
    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'
