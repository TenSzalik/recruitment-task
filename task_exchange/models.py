from django.db import models


class Currency(models.Model):
    code = models.CharField(
        max_length=3, unique=True, help_text="3-letter ISO 4217 code"
    )
    base_rate = models.DecimalField(
        max_digits=255,
        decimal_places=6,
        help_text="exchange rate relative to the base currency (USD)",
    )

    def __str__(self):
        return f"{self.code}: {self.base_rate}"

    class Meta:
        verbose_name_plural = "Currencies"
