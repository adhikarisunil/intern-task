from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if(password is not None):
            instance.set_password(password)  #This hides the password
            instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class FavoriteProductSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()