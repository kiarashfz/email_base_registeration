from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # make_password method hashed user password then save it in DB
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # make_password method hashed user password then save it in DB
        if validated_data.get('password'):  # check if it exists for patch method
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
