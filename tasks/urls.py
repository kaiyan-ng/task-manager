from django.urls import path, include
from . import views
from .views import TasksViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path("", views.index, name='index'),
    path("add", views.add, name='add'),
    path("api/", include(router.urls))
]