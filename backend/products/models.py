from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    """Category"""
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.CharField(max_length=300, verbose_name="Описание категории(по желанию)", null=True, blank=True)
    url = models.SlugField(max_length=50, verbose_name="Url", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """Single game product"""
    title = models.CharField(max_length=150, unique=True, verbose_name="Название игры")
    short_description = models.TextField(max_length=300, verbose_name="Краткое описание")
    poster = models.ImageField(upload_to="media/posters")
    description = RichTextField(verbose_name="Полное описание")
    categories = models.ManyToManyField("Category", related_name="games", verbose_name="Категории")
    year = models.PositiveSmallIntegerField(default=2014, verbose_name="Год выхода")
    age_limit = models.PositiveSmallIntegerField(default=3, verbose_name="Ограничения по возрасту")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")
    aviable = models.BooleanField(default=True, verbose_name="Доступность")
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Цена")
    url = models.SlugField(unique=True, null=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"