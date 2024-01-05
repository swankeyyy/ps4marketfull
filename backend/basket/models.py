from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket', verbose_name='Товар')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} | {self.product} | {self.quantity}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
