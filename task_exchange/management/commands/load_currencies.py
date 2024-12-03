import yfinance as yf
from django.core.management.base import BaseCommand

from task_exchange.models import Currency


class Command(BaseCommand):
    help = "Fetch exchange rates and store them in the database"

    def handle(self, *args, **kwargs):
        base_currency = "USD"
        currencies = ["EUR", "JPY", "PLN", "GBP", "AUD", "CAD", "CHF"]

        Currency.objects.update_or_create(
                code=base_currency,
                defaults={"base_rate": 1.0},
            )

        for code in currencies:
            try:
                ticker = yf.Ticker(f"{code}{base_currency}=X")
                current_price = ticker.history()["Close"].iloc[-1]
                Currency.objects.update_or_create(
                    code=code,
                    defaults={"base_rate": current_price},
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Saved rate for {code}: {current_price}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to retrieve rate for {code}: {e}")
                )
