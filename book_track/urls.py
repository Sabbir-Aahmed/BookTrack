
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

from django.shortcuts import redirect

def redirect_to_api_v1(request):
    return redirect('/api/v1/', permanent=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', redirect_to_api_v1),
    path('api/v1/', include('api.urls'), name='api-root'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
     
] + debug_toolbar_urls()