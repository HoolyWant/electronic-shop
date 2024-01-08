# Generated by Django 5.0.1 on 2024-01-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='linked_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ссылка на поставщика'),
        ),
        migrations.RemoveField(
            model_name='contact',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='product',
            name='provider',
        ),
        migrations.AddField(
            model_name='contact',
            name='provider',
            field=models.ManyToManyField(blank=True, null=True, related_name='contact', to='shop.provider', verbose_name='поставщик'),
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='shop.provider', verbose_name='поставщик'),
        ),
    ]