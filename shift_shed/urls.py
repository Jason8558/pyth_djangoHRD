from django.urls import path
from . import views
urlpatterns = [
path('', views.ss_main, name='ss-main'),
path('create/', views.ss_create, name='ss-create'),
path('getemps/<int:dep>', views.ss_get_employers, name='ss-emps'),
path('getemps/single/<int:id>', views.ss_get_emp_single, name='ss-emp'),
path('shedule/<int:id>', views.ss_shedule, name='ss-shedule'),
path('edit/<int:shed>/<int:month>/<int:year>', views.ss_edit, name='ss-edit'),
path('shedule/additem/<int:shed>/<int:month>', views.ss_item_add, name='ss-additem')

]
