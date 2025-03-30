from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path, include 

router = DefaultRouter()
router.register('', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]