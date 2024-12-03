import pytest
from rest_framework import status


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_currency_list(not_auth_client, currency):
    response = not_auth_client.get("/currency/")
    expected_response = [
        {"code": "PLN"},
        {"code": "EUR"},
        {"code": "USD"},
        {"code": "JPY"},
    ]

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
@pytest.mark.parametrize(
    "currency_pair, expected_response",
    [
        ("EUR/USD", {"currency_pair": "EURUSD", "exchange_rate": "1.04954"}),
        ("USD/EUR", {"currency_pair": "USDEUR", "exchange_rate": "0.95280"}),
        ("JPY/JPY", {"currency_pair": "JPYJPY", "exchange_rate": "1.00000"}),
    ],
)
def test_currency_retrieve(not_auth_client, currency, currency_pair, expected_response):
    response = not_auth_client.get(f"/currency/{currency_pair}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_currency_retrieve_FAIL_does_not_exist(not_auth_client, currency):
    response = not_auth_client.get("/currency/AAA/BBB/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"error": "One of the currencies does not exist."}


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_currency_retrieve_FAIL_too_long_code(not_auth_client, currency):
    response = not_auth_client.get("/currency/AAAA/BBBB/")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "Currency too long"}
