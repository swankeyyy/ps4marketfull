from django.db import models
from products.models import Product
from users.models import User


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comment', on_delete=models.CASCADE,
                                null=True, blank=True, verbose_name="Товар")
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name="Пользователь")
    body = models.TextField(max_length=300, verbose_name="Текст комментария", default="Введите текст")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} - {self.user}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'