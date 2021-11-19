from django.utils.translation import gettext_lazy as _

from rest_framework import viewsets
from rest_framework.response import Response

from app_example.models import Book
from app_example.serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Book to be viewed or edited.'''
    authentication_classes = []
    queryset = Book.objects.all()
    serializer_class = BookSerializer
