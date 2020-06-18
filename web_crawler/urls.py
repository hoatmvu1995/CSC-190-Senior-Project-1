"""web_crawler URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('output/', views.output,name="output"),
    path('default_crawler/', views.default_page,name="default_page"),
    path('admin_page/', views.admin_page,name="admin_page"),
    path('regular_page/', views.regular_page,name="regular_page"),
    path('pass_forgot/', views.pass_forgot,name="pass_forgot"),
    path('pass_change/', views.pass_change,name="pass_change"),
    path('pass_change_success/', views.pass_change_success,name="pass_change_success"),
    path('pass_found/', views.pass_found,name="pass_found"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
