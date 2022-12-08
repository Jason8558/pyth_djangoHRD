from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from . import views

urlpatterns = [
path('', views.vacsheds, name='vacshed_url'),
path('aup/', views.vacsheds_aup, name='vacshed_aup_url'),
path('new/', views.vacshed_new, name='new_vacshed_url'),
path('create/<int:vs>/', views.vacshed_create, name='vacshed_create_url'),
path('getvacshed/<int:vs>/', views.getvacshed_json, name='vacshed_json'),
path('itemadd/<int:id>', views.vacshed_addItem, name='additem_url'),
path('itemupd/<int:id>/<int:type>', views.vacshed_updItem, name='upditem_url'),
path('getemps/<int:dep>', views.getemployers, name='getemps_url'),
path('global/', views.vacshed_global_create, name='global_url'),
path('global/<str:year>/<int:dep>/<int:per>/<str:emps>/<int:fil_only>/<int:terr>/<str:pos>', views.vacshed_global_json, name='global_json_url'),
path('delitem/<int:id>', views.delitem, name='delitem_url'),
path('check/<int:id>', views.vacshed_check, name='check_url'),
path('empinfo/<str:year>/<int:emp>/', views.vacshed_emp_info, name='emp_info_url'),
]
