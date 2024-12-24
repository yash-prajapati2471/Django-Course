from django.urls import path,include
from rest_framework import routers
from .views import userview

router = routers.DefaultRouter()
router.register(r'user',userview)


urlpatterns = [
    path('',include(router.urls)),
]
