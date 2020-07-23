
from django.conf.urls import url, include
from rest_framework import routers
from app.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    url(r'app/', include(router.urls)),
]