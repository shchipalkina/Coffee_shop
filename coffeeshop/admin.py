from django.contrib import admin
from .db_models.drink import Drink
from .db_models.coffeeshop import CoffeeShop
from .db_models.cart import Cart
from .db_models.drinkorder import DrinkOrder


@admin.register(CoffeeShop)
class CoffeeShopAdmin(admin.ModelAdmin):

    list_display = ['name', 'id']
    search_fields = ('name',)


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'id']
    search_fields = ('name',)
    list_editable = ['price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['user_name', 'id']
    search_fields = ('user_name',)


@admin.register(DrinkOrder)
class DrinkOrderAdmin(admin.ModelAdmin):
    list_display = ['cart', 'quantity', 'drink', 'id']
    search_fields = ('order__user_name',)
