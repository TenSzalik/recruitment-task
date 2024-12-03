from rest_framework.routers import SimpleRouter, Route
from .views import CurrencyViewSet


class CurrencyCustomRouter(SimpleRouter):
    routes = [
        Route(
            url=r"^{prefix}$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        Route(
            url=r"^{prefix}/(?P<base_code>[^/.]+)/(?P<target_code>[^/.]+)/$",
            mapping={"get": "retrieve"},
            name="{basename}-retrieve",
            detail=True,
            initkwargs={"suffix": "Detail"},
        ),
    ]

router = CurrencyCustomRouter()
router.register(r"", CurrencyViewSet, basename="currency")
