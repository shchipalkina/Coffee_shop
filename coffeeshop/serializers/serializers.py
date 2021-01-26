from rest_framework import serializers
from coffeeshop.db_models.drink import Drink
from coffeeshop.db_models.coffeeshop import CoffeeShop
from coffeeshop.db_models.cart import Cart
from coffeeshop.db_models.drinkorder import DrinkOrder


class CoffeeShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeShop
        fields = '__all__'


class DrinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drink
        fields = '__all__'


class DrinkOrderSerializer(serializers.ModelSerializer):
    drink = serializers.CharField(source="drink.name")

    class Meta:
        model = DrinkOrder
        fields = ['id', 'drink', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    drinkorders = DrinkOrderSerializer(many=True, source="drinkorder_set")
    coffeeshop = serializers.CharField(source='coffeeshop.name')
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, object):
        return object.total_price

    class Meta:
        model = Cart
        fields = ['id', 'coffeeshop', 'user_name', 'drinkorders', 'total_price']


class DrinkOrderInCartPostSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = DrinkOrder
        fields = ['drink', 'quantity']


class DrinkOrderPostSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = DrinkOrder
        fields = ['cart', 'drink', 'quantity']


class CartPostSerializer(serializers.ModelSerializer):
    drinkorder_set = DrinkOrderInCartPostSerializer(many=True)

    def create(self, validated_data):
        drinkorder_data = validated_data["drinkorder_set"]
        validated_data.pop("drinkorder_set")
        cart = Cart.objects.create(**validated_data)

        for drinkorder in drinkorder_data:
            drinkorder["cart"] = cart
            DrinkOrder.objects.create(**drinkorder)
        return cart

    class Meta:
        model = Cart
        fields = ['id', 'coffeeshop', 'user_name', 'drinkorder_set']

