from django.urls import path
from . import views
urlpatterns = [
path('<str:year>', views.get_cal, name='wc-get'),

]
