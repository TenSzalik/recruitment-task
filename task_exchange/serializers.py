from rest_framework import serializers
from .models import Currency


class CurrencyReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["code"]


class ExchangeRateReadSerializer(serializers.Serializer):
    currency_pair = serializers.CharField()
    exchange_rate = serializers.DecimalField(max_digits=24, decimal_places=5)
