from django.shortcuts import render
from rest_framework import viewsets
from .models import Link
from .serilizer import LinkSerlizer


class PostListApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(viewsets.ModelViewSet):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(viewsets.ModelViewSet):
    queryset= Link.objects.filter(active=True)
    serializer_class = LinkSerializer

# Create your views here.
