from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DepartmentViewSet, DoctorViewSet

router = DefaultRouter()
router.register(r'doctor', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('departments/<uuid:pk>/doctors/', DoctorViewSet.as_view({'get': 'list'}), name='department-doctors'),
    path('departments/<uuid:pk>/patients/', PatientViewSet.as_view({'get': 'list'}), name='department-patients'),
]
