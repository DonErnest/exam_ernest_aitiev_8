from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Автор отзыва')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Продукт')
    review = models.TextField(max_length=1500, null=False, blank=False, verbose_name='Отзыв')
    rating = models.PositiveIntegerField(null=False, blank=False,
                                         validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Оценка')

    def __str__(self):
        return "Отзыв пользователя {} о {}".format(self.author, self.product)
