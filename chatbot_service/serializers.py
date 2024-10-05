from rest_framework import serializers
from .models import UserQuery


class UerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuery
        fields = "__all__"