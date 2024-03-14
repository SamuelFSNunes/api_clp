from rest_framework import serializers
from .models import JSONCLP

class JSONSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONCLP
        fields = '__all__'