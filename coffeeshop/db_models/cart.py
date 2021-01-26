from django.db import models
from .coffeeshop import CoffeeShop


class Cart(models.Model):

    user_name = models.CharField('Имя', max_length=100)
    coffeeshop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name='cafe_name', null=True)

    @property
    def total_price(self):
        total_price = 0
        if len(self.drinkorder_set.all()) > 0:
            for drinkorder in self.drinkorder_set.all():
                total_price += drinkorder.quantity * drinkorder.drink.price
        return total_price

    total_price.fget.short_description = "конечная стоимость заказа"

    def __str__(self):
        return self.user_name
