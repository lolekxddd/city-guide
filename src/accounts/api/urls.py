from django.urls import path, include, re_path
from rest_framework import routers
from .views import UserViewSet
from rest_auth.registration.views import VerifyEmailView, RegisterView

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/register', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
]