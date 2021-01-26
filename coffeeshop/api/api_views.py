from rest_framework import generics
from rest_framework.viewsets import *
from rest_framework.response import Response
from rest_framework.mixins import DestroyModelMixin
from coffeeshop.serializers.serializers import CoffeeShopSerializer, DrinkSerializer, CartSerializer, DrinkOrderSerializer, CartPostSerializer, DrinkOrderPostSerializer
from ..db_models.coffeeshop import CoffeeShop
from ..db_models.cart import Cart
from ..db_models.drink import Drink
from ..db_models.drinkorder import DrinkOrder


# Метод списка кофешопов, должен вернуть список имеющихся кофешопов.
class CoffeeListAPIView(generics.ListCreateAPIView):

    serializer_class = CoffeeShopSerializer
    queryset = CoffeeShop.objects.all()


# Метод списка напитков, должен вернуть список имеющихся напитков.
class DrinkListAPIView(generics.ListCreateAPIView):

    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


# Метод списка заказов, возвращает все заказы по кофешопу.
class CartAPIView(ViewSetMixin, generics.ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CartSerializer
        elif self.request.method == 'POST':
            return CartPostSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Cart.objects.all()
            coffeeshop = self.request.GET.get('coffeeshop', None)
            user_name = self.request.GET.get('user_name', None)
            id = self.request.GET.get('id', None)
            if coffeeshop is not None:
                queryset = queryset.filter(coffeeshop__name=coffeeshop)
            elif user_name is not None:
                queryset = queryset.filter(user_name=user_name)
            elif id is not None:
                queryset = queryset.filter(id=id)
            return queryset


class CartDeleteAPIView(DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()


# Метод создания заказа, возвращает заказ с позициями.
class DrinkOrderAPIView(ViewSetMixin, generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DrinkOrderSerializer
        elif self.request.method == 'POST':
            return DrinkOrderPostSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = DrinkOrder.objects.all()
            user_name = self.request.GET.get('q', None)
            if user_name is not None:
                queryset = queryset.filter(user_name=user_name)
        return queryset

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                cartdrink = DrinkOrder.objects.get(id=id)
                serializer = DrinkOrderSerializer(cartdrink)
        except:
            cartdrinks = self.get_queryset()
            serializer = DrinkOrderSerializer(cartdrinks, many=True)

        return Response(serializer.data)


class DrinkOrderDeleteAPIView(DestroyModelMixin, GenericViewSet):
    queryset = DrinkOrder.objects.all()
