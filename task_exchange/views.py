from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Currency
from .serializers import CurrencyReadSerializer, ExchangeRateReadSerializer


class CurrencyViewSet(ViewSet):
    def list(self, request):
        """
        Returns a list of all currencies.
        """
        currencies = Currency.objects.all()
        serializer = CurrencyReadSerializer(currencies, many=True)
        return Response(serializer.data)

    def retrieve(self, request, base_code=None, target_code=None):
        """
        Returns the latest exchange rate for a currency pair.
        """
        if (len(base_code) != 3) or (len(target_code) != 3):
            return Response(
                {"error": "Currency too long"},
                status=400,
            )
        try:
            base_cur_obj = Currency.objects.get(code=base_code)
            target_cur_obj = Currency.objects.get(code=target_code)
            serializer = ExchangeRateReadSerializer(
                {
                    "currency_pair": f"{base_code}{target_code}",
                    "exchange_rate": base_cur_obj.base_rate
                    / target_cur_obj.base_rate,
                }
            )
            return Response(serializer.data)
        except Currency.DoesNotExist:
            return Response(
                {"error": "One of the currencies does not exist."},
                status=404,
            )
