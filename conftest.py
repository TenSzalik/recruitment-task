from decimal import Decimal
from itertools import cycle

import pytest
from model_bakery.recipe import Recipe

from task_exchange.models import Currency
from rest_framework.test import APIClient


@pytest.fixture(name="not_auth_client")
def fixture_not_auth_client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture(name="currency")
def fixture_currency():
    return Recipe(
        Currency,
        code=cycle(["PLN", "EUR", "USD", "JPY"]),
        base_rate=cycle(
            [
                Decimal("0.244901"),
                Decimal("1.049538"),
                Decimal("1.000000"),
                Decimal("0.006698"),
            ]
        ),
        _quantity=4,
    ).make()
