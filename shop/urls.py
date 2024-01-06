from django.urls import path

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('lesson/', ProviderAPIList.as_view(), name='lesson_list'),
]
