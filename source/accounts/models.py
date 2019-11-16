from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True, blank=False, verbose_name='Автор отзыва')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews', null=False, blank=False, verbose_name='Продукт')
    review = models.TextField(max_length=1500, null=False, blank=False, verbose_name='Отзыв')
    rating = models.PositiveIntegerField(null=False, blank=False,
                                         validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')

    def __str__(self):
        return "Отзыв пользователя {} о {}".format(self.author, self.product)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avs', verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'