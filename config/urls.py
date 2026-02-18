from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet
from applications.views import ApplicationViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("jobs", JobViewSet)
router.register("applications", ApplicationViewSet)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
]
