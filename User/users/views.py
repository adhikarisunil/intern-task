from multiprocessing import AuthenticationError
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import FavoriteProductSerializer, UsersSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from .producer import publish
from users import serializers
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    

# class UsersViewset(viewsets.ViewSet):
    # def list(self, request):
    #     user = Users.objects.all()
    #     serializer = UsersSerializer(user, many=True)
    #     publish()
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        products = Users.objects.all()
        serializer = UsersSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('users_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Users.objects.get(pk=pk)
        serializer = UsersSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = Users.objects.get(pk=pk)
        serializer = UsersSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('users_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        product = Users.objects.get(pk=pk)
        product.delete()
        publish('users_deleted', pk)
        return Response('Users deleted')


class UserProfileView(TokenObtainPairView):
    # permission_classes = [IsAuthenticated]


    
    def post(self,request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data['access']
        refresh_token = response.data['refresh']
        token = RefreshToken(refresh_token)

        response =  Response({
            'access_token':access_token,
            'refresh_token':str(refresh_token),
            # 'id':token.payload['user_id'],
            # 'username':UserProfileView.objects.get(id=token.payload['user_id']).username,
            # 'email': UserProfileView.objects.get(id=token.payload['user_id']).email
        })

        # setting access and refresh token in cookie
        response.set_cookie('access_token',access_token, httponly=True)
        response.set_cookie('refresh_token',refresh_token, httponly=True)
        return response


class FavoriteProductViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = FavoriteProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user_id']  # Temporarily using a fixed user ID for testing
        product_id = serializer.validated_data['product_id']

        # Publish the message to RabbitMQ
        publish(user_id, product_id)

        return Response({'message': 'Favorite product request sent'})