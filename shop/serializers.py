import os

from rest_framework import serializers

from shop.models import Provider, Product, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['provider', 'email', 'country', 'city', 'street', 'house', ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['provider', 'title', 'model', 'launch_date', ]


class ProviderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    debt = serializers.IntegerField(read_only=True)
    # provider_link = serializers.SerializerMethodField()

    # def get_link(self, obj):
    #     if self.request.user.is_superuser == True:
    #         return os.getenv('HOST_DOMEN') + '/providers/' + obj.linked.id

    class Meta:
        model = Provider
        fields = ['id', 'title', 'contact', 'linked', 'products', 'debt', 'create_date', 'level', ]
