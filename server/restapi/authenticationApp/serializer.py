from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            username = validated_data['username'], 
            email = validated_data['email'], 
            password = validated_data['password'])
        
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
        
