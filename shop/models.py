from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Provider(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    linked = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    debt = models.PositiveIntegerField(default=0, verbose_name='задолженность')
    level = models.PositiveIntegerField(default=0, verbose_name='уровень иерархии')


class Product(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, **NULLABLE,
                                 related_name='products', verbose_name='поставщик')
    title = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    launch_date = models.DateField(verbose_name='дата выхода продукта на рынок')


class Contact(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, **NULLABLE,
                                 related_name='contact', verbose_name='поставщик')
    title = models.CharField(max_length=100, verbose_name='название')
    email = models.CharField(max_length=100, verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house = models.CharField(max_length=100, verbose_name='дом')
