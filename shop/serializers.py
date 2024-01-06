import os

from rest_framework import serializers

from shop.models import Provider


class ContactSerializer(serializers.Serializer):
    pass


class ProductSerializer(serializers.Serializer):
    pass


class ProviderSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    contact = ContactSerializer(many=False)
    provider_link = serializers.SerializerMethodField()
    level = serializers.CharField(read_only=True)

    # def get_link(self, obj):
    #     if self.request.user.is_superuser == True:
    #         return os.getenv('HOST_DOMEN') + '/providers/' + obj.linked.id

    class Meta:
        model = Provider
        fields = ['title', 'contact', 'products', 'debt', 'create_date', 'level', ]
