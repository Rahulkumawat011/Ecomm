from django.urls import path, include
from rest_framework import routers
from apps.user.rest_api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

