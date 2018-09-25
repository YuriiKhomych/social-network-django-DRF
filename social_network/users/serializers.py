from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Class based on User model and
        describes the all fields from User model.
    """
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
