from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    # class Meta:
    #     model = User
    #     fields = ['id', 'username']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')


class DebtMonetarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtMonetary
        fields = ('__all__')


class DebtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtItem
        fields = ('__all__')
