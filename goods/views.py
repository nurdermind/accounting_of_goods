from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .mixins import IncreaseActionMixin, ReduceActionMixin
from .models import Good
from .serializer import GoodSerializer, GoodIncreaseSerializer, GoodReduceSerializer


class GoodViewSet(viewsets.ModelViewSet, IncreaseActionMixin, ReduceActionMixin):
    permissions = [IsAuthenticatedOrReadOnly]
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    extra_serializers = {
        'increase': GoodIncreaseSerializer,
        'reduce': GoodReduceSerializer,
    }
