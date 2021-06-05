from .views import EmployeeViewSet, WorksiteViewSet, ItemViewSet
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'employee', views.EmployeeViewSet, "employee")
router.register(r'worksite', views.WorksiteViewSet, "worksite")
router.register(r'item', views.ItemViewSet, "item")

urlpatterns = [
    path('', include(router.urls))
    
    
]

