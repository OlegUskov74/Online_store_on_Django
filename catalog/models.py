from django.db import models


class Category(models.Model):
    """Модель Category"""

    name = models.CharField(
        max_length=200,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание",
    )

    def __str__(self):
        """Вывод информации"""

        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]


class Product(models.Model):
    """Модель Product"""

    name = models.CharField(
        max_length=200,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        null=True,
        verbose_name="Цена",
        help_text="Введите цену продукта",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        """Вывод информации"""

        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
        ]  # сортировка
