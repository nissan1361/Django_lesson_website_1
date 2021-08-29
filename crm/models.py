from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=80, verbose_name='имя')
    order_phone = models.CharField(max_length=40, verbose_name='телефон')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
