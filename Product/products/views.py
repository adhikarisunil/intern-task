
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
# from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, FavoriteSerializer
# from .consumer import publish
from rest_framework.decorators import api_view

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer


    # def get(self, request):
    #     user = request.user
    #     serializer = FavoriteSerializer(user)
    #     return Response(serializer.data)

# @api_view(['GET'])
# def product(request, pk, format=None):

#     query = {'username': 'ram'}
#     req = request.get('http://127.0.0.1:8000/users', params=query)
#     data = req.json()
#     print(data)


#     try:
#         for s in range(len(data)):
#             if data[s]['id']:
#                 favorite = Favorite.objects.create(user_id=data[s]['id'], quote_id=pk)
#                 favorite.save()
#                 publish('product_liked', pk)
#                 print('Favorite created')
#                 return Response('Product liked...', status=status.HTTP_201_CREATED)
#     except:

#         return Response("Product liked...",status=status.HTTP_400_BAD_REQUEST)