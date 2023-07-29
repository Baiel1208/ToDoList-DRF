from rest_framework import serializers
from django.contrib.auth import password_validation

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age',
                'date_joined')


# Регистрация
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        model = User
        fields = ('id',  'username', 'email', 
                'phone_number', 'age','date_joined','password', 'confirm_password')


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        # Используйте функцию validate_password, чтобы применить все валидаторы пароля.
        password_validation.validate_password(attrs['password'], self.instance)
        # phone number 
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError('Номер телефона должен быть в формате +996*********')
        return attrs


    def create(self, validated_data: dict):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data['age'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])

        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name',
                'last_name', 'email', 'phone_number', 'age',
                'date_joined',)
