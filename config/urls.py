from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularSwaggerView, 
    SpectacularRedocView
)




urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas da API
    path('api/', include('apps.professionals.urls')), 
    path('api/', include('apps.appointments.urls')),
    
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Gera o arquivo esquema (JSON/YAML)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Interface Visual Swagger
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Interface Visual Redoc
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]