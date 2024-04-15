from rest_framework import serializers
from django.contrib.auth.models import User


class ConsumerRegisterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','password','username']
