from django.db import models
from .cart import Cart
from .drink import Drink


class DrinkOrder(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '%s %d' % (self.drink, self.quantity)
