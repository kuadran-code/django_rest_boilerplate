from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
