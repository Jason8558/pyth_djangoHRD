from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outbound_docs/', views.outbound_docs, name='outbound')
]
