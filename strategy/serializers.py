from rest_framework import serializers
from .models import Entrepreneur

class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = ['name', 'company', 'expertise', 'image', 'industry']

        