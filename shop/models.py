from django.db import models

NULLABLE = {'blank': True, 'null': True}


class StoreChain(models.Model):
    title = models.CharField()
    email = models.CharField()
    country = models.CharField()
    city = models.CharField()
    street = models.CharField()
    house = models.CharField()
    provider = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
