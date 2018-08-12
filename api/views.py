from django.shortcuts import render
from rest_framework import generics
from items.models import *
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import *

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter,]
    search_fields = ['name', 'description',]

class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'