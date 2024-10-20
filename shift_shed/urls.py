from django.urls import path
from . import views
urlpatterns = [
path('', views.ss_main, name='ss-main'),
path('create/', views.ss_create, name='ss-create'),
path('getemps/<int:dep>', views.ss_get_employers, name='ss-emps'),
path('getemps/single/<int:id>', views.ss_get_emp_single, name='ss-emp'),
path('shedule/<int:id>', views.ss_shedule, name='ss-shedule'),
# path('shedule/<int:id>/print', views.ss_print, name='ss-print'),
path('edit/<int:shed>/<int:month>/<int:year>', views.ss_edit, name='ss-edit'),
path('shedule/additem/<int:shed>/<int:month>', views.ss_item_add, name='ss-additem'),
#path('getvac/<int:emp>/<int:year>/<int:month>', views.ss_get_vacantions, name='ss-getvac'),
path('shedule/upditem/<int:id>', views.ss_item_upd, name='ss-upditem'),
path('shedule/checked/<int:id>', views.ss_set_checked, name='ss-setcheck'),
path('shedule/removeitem/<int:id>', views.ss_item_remove, name='ss-removeitem'),
path('shedule/setcomm/<int:id>', views.ss_change_comment, name='ss-changecomm'),

]
