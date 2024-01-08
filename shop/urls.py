from rest_framework.routers import DefaultRouter

from shop.apps import ShopConfig
from shop.views import ProductViewSet, ContactViewSet, ProviderViewSet

app_name = ShopConfig.name

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'provider', ProviderViewSet, basename='provider')

urlpatterns = [
] + router.urls
