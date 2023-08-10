from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, FavoriteViewSet
# from rest_framework_simplejwt.views import TokenVerifyView

from . import views
router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]