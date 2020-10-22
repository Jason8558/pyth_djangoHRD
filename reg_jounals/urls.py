from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outbound_docs/', views.outbound_docs, name='outbound'),
    path('outbound_docs/add', views.nr_OutBoundDocument, name='doc_outbound_add_url'),
    path('letters_of_resignation/', views.letter_of_resignation, name='resignation'),
    path('letters_of_invite/', views.letter_of_invite, name='invite'),
    path('letters_of_invite/add', views.nr_LetterOfInvite, name='invite_add')
]
