from django.db import models
from .drink import Drink


class CoffeeShop(models.Model):

    name = models.CharField(max_length=100, db_index=True, verbose_name='Название кофейни')
    image = models.ImageField(verbose_name='Image', upload_to='cafe/', null=True, blank=True)
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return self.name
