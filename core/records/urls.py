from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DepartmentViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
