from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outbound_docs/', views.outbound_docs, name='outbound'),
    path('outbound_docs/add', views.nr_OutBoundDocument, name='doc_outbound_add_url'),
    path('outbound_docs/<int:id>/edit', views.upd_OutBoundDocument, name='doc_outbound_upd_url'),
    path('outbound_docs/<int:id>/del', views.del_OutBoundDocument, name='doc_outbound_del_url'),
    path('letters_of_resignation/', views.letter_of_resignation, name='resignation'),
    path('letters_of_resignation/add', views.nr_LetterOfResignation, name='letter_resignation_add_url'),
    path('letters_of_resignation/<int:id>/edit', views.upd_LetterOfResignation, name='letter_resignation_upd_url'),
    path('letters_of_resignation/<int:id>/del', views.del_LetterOfResignation, name='letter_resignation_del_url'),
    path('letters_of_invite/', views.letter_of_invite, name='invite'),
    path('letters_of_invite/add', views.nr_LetterOfInvite, name='invite_add'),
    path('letters_of_invite/<int:id>/edit', views.upd_LetterOfInvite, name='invite_upd_url'),
    path('letters_of_invite/<int:id>/del', views.del_LetterOfInvite, name='invite_del_url'),
    path('orders_on_others/', views.order_other_matters, name='orders_on_others'),
    path('orders_on_others/add', views.nr_OrderOnOtherMatters, name='orders_on_others_add_url'),
    path('orders_on_others/<int:id>/edit', views.upd_OrderOnOtherMatters, name='orders_on_others_upd_url'),
    path('orders_on_others/<int:id>/del', views.del_OrderOnOtherMatters, name='orders_on_others_del_url'),
    path('orders_on_vacation/', views.order_on_vacation, name='orders_on_vacation'),
    path('orders_on_vacation/add', views.nr_OrderOnVacation, name='orders_on_vacation_add_url'),
    path('orders_on_vacation/<int:id>/upd', views.upd_OrderOnVacation, name='orders_on_vacation_upd_url'),
    path('orders_on_vacation/<int:id>/del', views.del_OrderOnVacation, name='orders_on_vacation_del_url'),
    path('orders_of_BTrip/', views.order_of_BTrip, name='orders_of_BTrip'),
    path('orders_of_BTrip/add', views.nr_OrderOfBTrip, name='orders_of_BTrip_add_url')
    ]
