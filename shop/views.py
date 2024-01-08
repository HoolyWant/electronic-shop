from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from shop.models import Product, Contact, Provider
from shop.serializers import ProductSerializer, ContactSerializer, ProviderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = (, )


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    @action(detail=True, methods=['GET'])
    def clean_debt(self, request, pk=None):
        try:
            provider = self.get_object()
            if request.user.is_superuser == True:
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

