from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewSet

router = DefaultRouter()
router.register(r'jobapplications', JobApplicationViewSet, basename='jobapplication')

urlpatterns = [
    #path('create/', JobApplicationViewSet.as_view({'post': 'create'}), name='create'),
]

urlpatterns += router.urls
