"""connect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import home_view


urlpatterns = [

    path('', home_view, name='home-view'),
    path('admin/', admin.site.urls),
    path('nested_admin', include('nested_admin.urls')),
    path('', include('account.urls')),
    path('', include('employee.urls')),
    path('', include('employer.urls')),
    path('', include('personality.urls')),
    path('api-auth/', include('rest_framework.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
