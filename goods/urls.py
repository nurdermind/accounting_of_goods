# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path, include
from rest_framework import routers
from .views import GoodViewSet

router = routers.DefaultRouter()
router.register(r'goods', GoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
