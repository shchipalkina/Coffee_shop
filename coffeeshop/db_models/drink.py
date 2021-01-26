from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal


class Drink(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField('Состав', max_length=250, blank=True, null=True)
    image = models.ImageField(verbose_name='Image', upload_to='coffee/', null=True, blank=True)
    price = models.FloatField(max_length=10, validators=[MinValueValidator(Decimal(0))])

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        super(Drink, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
