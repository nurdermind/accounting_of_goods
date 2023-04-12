from django.shortcuts import render
from rest_framework import viewsets
from .models import Good
from .serializer import GoodSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
