from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

INTERVAL_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (10, "10"),
    (12, "12"),
    (15, "15"),
    (20, "20"),
    (30, "30"),
    (60, "60"),
)

VALUE_CHOICES = (("F", "Foo"), ("B", "Bar"), ("BZ", "Baz"))


class Thing(models.Model):
    name = models.CharField(
        "thing name",
        help_text="The name of the thing. This should be unique.",
        max_length=200,
        unique=True,
    )

    number = models.PositiveIntegerField(
        default=2,
        help_text="This has a defined default, min, and max value",
        validators=[MinValueValidator(0), MaxValueValidator(1500)],
    )

    interval = models.PositiveIntegerField(
        "interval (minutes)", default=60, choices=INTERVAL_CHOICES
    )

    value = models.CharField(max_length=10, choices=VALUE_CHOICES, default="B")
