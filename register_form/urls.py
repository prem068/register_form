"""
URL configuration for register_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',display),
    path('insert/',insert_view),
    path('update/<str:id>',update_view),
    path('delete/<str:id>',delete_view),
    #api--calls
    path('api/employees/', api_display, name='api_display'),
    path('api/employees/insert/', api_insert, name='api_insert'),
    path('api/employees/delete/<int:id>/', api_delete, name='api_delete'),
    path('api/employees/update/<int:id>/', api_update, name='api_update')
]

