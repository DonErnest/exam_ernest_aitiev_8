from django.db import models
from django.db.models import Sum, Avg
from math import modf

from accounts.models import Review

CATEGORY_DEFAULT = 'other'

CATEGORY_CHOICES = [('food', 'Еда'),('leisure', 'Развлечения'),
                    ('household', 'Для дома'),('hobby', 'Хобби'),
                    (CATEGORY_DEFAULT, 'Разное')]

class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='Наименование продукта/услуги')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_DEFAULT, null=False, blank=False, verbose_name='Категория')
    description = models.TextField(max_length=1500, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='uploads', null=True, blank=True, verbose_name='Изображение')

    def average(self):

        average = self.reviews.aggregate(average=Avg('rating'))
        if average['average']:
            average_parts = modf(average['average'])
            average['wholes'] = int(average_parts[1])
            average['decimal'] = 100 - average_parts[0]*100
            average['rest'] = average_parts[0]*100
            average['shift'] = 18*average['decimal']//100
            return average
        else:
            return None


    def __str__(self):
        return self.name
