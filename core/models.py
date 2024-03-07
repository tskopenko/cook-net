from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ["last_name"]
        verbose_name_plural = "cooks"
        verbose_name = "cook"

    def __str__(self):
        return f"Mr. {self.last_name} ({self.username})"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"It is: {self.name}"
