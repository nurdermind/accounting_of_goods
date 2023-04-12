from django.urls import path, include
from .models import Good
from rest_framework import routers, serializers, viewsets


class GoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class GoodIncreaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Good
        fields = ('stock',)


class GoodReduceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Good
        fields = ('stock',)
