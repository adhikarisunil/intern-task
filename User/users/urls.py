from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, UsersViewSet, FavoriteProductViewSet
from rest_framework_simplejwt.views import TokenVerifyView

from . import views
router = DefaultRouter()
router.register('users', views.UsersViewSet, basename='users')
router.register(r'favorite-products', FavoriteProductViewSet, basename='favorite-product')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', UserProfileView.as_view())
]   