from django.contrib import admin
from django.urls import path, include, re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.api.urls')),
    path('api/attraction/', include(('attraction.api.urls', 'attraction.api')),
    path('api/plan/', include(('plan.api.urls', 'plan.api')),
]
