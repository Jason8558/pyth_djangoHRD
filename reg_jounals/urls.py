from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outbound_docs/', views.outbound_docs, name='outbound'),
    path('outbound_docs/add', views.nr_OutBoundDocument, name='doc_outbound_add_url')
]
