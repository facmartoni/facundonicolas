"""facundonicolas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

# Own

from facundonicolas import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace="posts")),
    path('wip', main_views.wip, name='wip'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [re_path(r'^.*$', main_views.not_found, name='not_found')]
