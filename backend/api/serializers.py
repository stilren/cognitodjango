from rest_framework import serializers
from .models import Chore

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chore
        fields = ('id', 'name')