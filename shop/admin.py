from django.contrib import admin

from shop.models import Provider, Product, Contact


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contact', 'linked', 'linked_url', 'debt', 'create_date', 'level', ]
    list_filter = ('contact__city', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'country', 'city', 'street', 'house', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['provider', 'title', 'model', 'launch_date', ]
