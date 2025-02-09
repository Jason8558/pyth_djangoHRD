"""hrd_docFlow URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views
from reg_jounals.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reg_jounals.urls')),
    path('vacshed/', include('vac_shed.urls')),
    path('turv/', include('TURV.urls')),
    path('shift_shed/', include('shift_shed.urls')),
    path('work_cal/', include('work_cal.urls')),
    path('vacshed/', include('vac_shed.urls')),
    path('accounts/login/', views.LoginView.as_view(template_name="registration/login.html",authentication_form=UserLoginForm),name='login'),
    path('accounts/', include('django.contrib.auth.urls'))]
