from django.urls import path, include
from rest_framework import routers
from apps.store.store_rest_api.views import StoreViewSet

router = routers.DefaultRouter()
router.register(r'store', StoreViewSet)

urlpatterns =[
    path('', include(router.urls)),

]