from django.urls import path
from . import views

urlpatterns = [
path('<str:year>', views.get_cal, name='wc-get'),
path('<str:year>/html/', views.get_cal_html, name='wc-get-html'),
path('<str:year>/html/upd', views.upd_record, name='wc-upd'),
path('<str:year>/html/clear', views.clear, name='wc-clear'),
path('<str:year>/<str:month>', views.get_month, name='wc-month'),
path('write/', views.new_record, name='wc-newrecord'),
path('', views.calendar_list, name='wc-list'),
# path('api/v1/getcal', WorkCalAPI.as_view())


]
