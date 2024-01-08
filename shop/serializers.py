import os

from rest_framework import serializers

from shop.models import Provider, Product, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'country', 'city', 'street', 'house', ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'model', 'launch_date', ]


class ProviderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    contact_info = ContactSerializer(source='contact', read_only=True)
    debt = serializers.IntegerField(read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'title', 'linked', 'contact', 'contact_info', 'product', 'debt', 'create_date', 'level', ]
