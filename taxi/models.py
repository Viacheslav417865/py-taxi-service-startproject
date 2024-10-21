from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username


class Car(models.Model):
    license_number = models.CharField(max_length=100, unique=True, null=True)
    manufacturer_name = models.CharField(max_length=100, null=True)
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.model
