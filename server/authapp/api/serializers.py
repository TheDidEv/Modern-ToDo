from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

        def create (self, validated_data):
            # create new user
            user = User.objecs.create_user(
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user