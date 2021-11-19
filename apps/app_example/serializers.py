from rest_framework import serializers
import os
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    '''Book Serializer'''
    class Meta:
        model = Book
        fields = '__all__'