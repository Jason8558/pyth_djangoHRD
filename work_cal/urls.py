from django.urls import path
from . import views
urlpatterns = [
path('<str:year>', views.get_cal, name='wc-get'),
path('<str:year>/<str:month>', views.get_month, name='wc-month')

]
