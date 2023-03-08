from dataclasses import fields
from .models import Student1
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'
