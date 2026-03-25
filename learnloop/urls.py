

"""
URL configuration for learnloop project.
Agentic AI Learning Platform - API Endpoints
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI documentation configuration
schema_view = get_schema_view(
    openapi.Info(
        title="LearnLoop API",
        default_version='v1',
        description="Agentic AI Learning Platform API - Demonstrates agent orchestration, evaluation frameworks, and real-time interaction analysis",
        contact=openapi.Contact(email="prince.eklu@proton.me"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # =============================================================================
    # ADMIN INTERFACE
    # =============================================================================
    path('admin/', admin.site.urls, name='admin'),

    # =============================================================================
    # API DOCUMENTATION (Swagger & Redoc)
    # =============================================================================
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # =============================================================================
    # CORE API ENDPOINTS (v1)
    # =============================================================================
    path('api/v1/', include('core.urls')),

    # =============================================================================
    # HEALTH CHECK & MONITORING
    # =============================================================================
    path('api/health/', lambda request: {'status': 'healthy', 'timestamp': 'now'}, name='health-check'),

    # =============================================================================
    # DJANGO REST FRAMEWORK (for browsable API)
    # =============================================================================
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
