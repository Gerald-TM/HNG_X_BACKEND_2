"""
URL configuration for hng_x project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view( # new
    openapi.Info(
        title="Person API",
        default_version="v1",
        description="A simple REST API that performs CRUD operations on person model",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="taiyemusa1582@gmail.com"),
        license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('restapi.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( # new
'redoc', cache_timeout=0), name='schema-redoc'),
]
