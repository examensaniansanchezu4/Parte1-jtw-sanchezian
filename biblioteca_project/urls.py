"""
URL configuration for biblioteca_project project.

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
# biblioteca_project/urls.py

from django.contrib import admin
from django.urls import path, include
from libros.jwt_views import CustomTokenObtainPairView
from libros import web_views 
urlpatterns = [
    # Admin de Django
    path('admin/', admin.site.urls),
    
    # ✨ URLs de la API (AGREGAR ESTA LÍNEA)
    path('api/',include('libros.api_urls')),

     # URLs de páginas web (para pruebas)
    path('', web_views.home, name='home'),
    path('oauth/login/', web_views.oauth_login, name='oauth_login'),
    path('login/jwt/', web_views.jwt_login_page, name='jwt_login_page'),
    
     # JWT personalizado
    path('auth/jwt/login/', CustomTokenObtainPairView.as_view(), name='jwt_login'),

     # ← AGREGAR: OAuth 2.0 URLs de django-oauth-toolkit
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]