from django.urls import path
from rest_framework.routers import SimpleRouter
from .api.api_views import CoffeeListAPIView, DrinkListAPIView, CartAPIView, DrinkOrderAPIView, DrinkOrderDeleteAPIView, CartDeleteAPIView

router = SimpleRouter()
router.register(r"carts", CartAPIView, basename="carts")
router.register(r"carts", CartDeleteAPIView, basename="carts")
router.register(r"drinkorders", DrinkOrderAPIView, basename="drinkorders")
router.register(r"drinkorders", DrinkOrderDeleteAPIView, basename="drinkorders")

urlpatterns = [
    path('coffeeshops/', CoffeeListAPIView.as_view(), name='coffeeshops'),
    path('drinks/', DrinkListAPIView.as_view(), name='drinks'),
]

urlpatterns += router.urls
