from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.contrib.auth import views
from .routers import router
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('testeg.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/',include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
