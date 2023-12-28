from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.CharField(max_length=300, verbose_name="Описание категории(по желанию)", null=True, blank=True)
    url = models.SlugField(max_length=50, verbose_name="Url", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'
