import os

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from shop.models import Product, Contact, Provider
from shop.permissions import IsActive
from shop.serializers import ProductSerializer, ContactSerializer, ProviderSerializer, ProviderSerializerWithoutDebt


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsActive,)


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = (IsActive,)


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    filter_backends = [SearchFilter,]
    search_fields = ['contact__country']
    permission_classes = (IsActive,)

    @action(detail=True, methods=['GET'])
    def clean_debt(self, request):
        try:
            provider = self.get_object()
            if request.user.is_superuser:
                provider.debt = 0
                provider.save()
                return Response({"success": "Provider's debt has been cleaned."}, status=200)
            else:
                return Response({"error": "You don't have permissions for this action"}, status=403)
        except Provider.DoesNotExist:
            return Response({"error": "Provider not found."}, status=404)

    def perform_create(self, serializer):
        new_provider = serializer.save()
        new_provider.level = Provider.objects.get(id=new_provider.linked_id).level + 1
        new_provider.save()

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            serializer_class = ProviderSerializerWithoutDebt

        return serializer_class
