"""nxtbn URL Configuration

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
import sys
from django.http import HttpResponse
from django.conf import settings
from django.urls import re_path, path
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView





# showing exact error in remote development server
if getattr(settings, 'DEVELOPMENT_SERVER') and not getattr(settings, 'DEBUG'):
    ''' Response very short details error during staging server and when debug=False '''
    def short_technical_response(request, exc_type, exc_value, tb, status_code=500):
        return HttpResponse(exc_value, status=status_code)

    def handler500(request):
        return short_technical_response(request, *sys.exc_info())


# Admin placeholder change
admin.site.site_header = "nxtbn"
admin.site.site_title = "nxtbn Admin Panel"
admin.site.index_title = "nxtbn Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nxtbn.home.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('users/', include('nxtbn.users.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='account/profile.html'), name='account_profiles'),
    path('user/v1/api/', include('nxtbn.users.api.v1.urls')),
    path('core/', include('nxtbn.core.api.v1.urls')),
]


API_INFO = openapi.Info(
    title="nxtbn API",
    default_version="v1",
    description="API documentation for nxtbn App",
)

API_DOCS_SCHEMA_VIEWS = get_schema_view(
    API_INFO,
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns += [
    path("api-playground/", API_DOCS_SCHEMA_VIEWS.with_ui("swagger", cache_timeout=0), name="api_playground")
]
