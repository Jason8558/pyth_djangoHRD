from .models import VacantionShedule as VacationShedules, VacantionSheduleItem as VacShedItems
from TURV.models import Department as TurvDepartments
import datetime as DT
from django.db.models import Q
from django.http import JsonResponse

def main_search(fields):

    department  = fields['department']
    year        = fields['year']

    search_result = VacationShedules.objects.all()

    if year:
        search_result = search_result.filter(year=year)

    if department:
        search_result = search_result.filter(dep=department)

    if not year and not department:
        search_result = []
    
    return(search_result)

def vacshed_global(request):
    search_query = {
        'year':        request.GET.get('vs-glob-year',     DT.datetime.now().year),
        'department':  request.GET.get('vs-glob-dep',      ''),
        'position':    request.GET.get('vs-glob-pos',      ''),
        'filial':      request.GET.get('vs-glob-fil',      ''),
        'territory':   request.GET.get('vs-glob-terr',     ''),
        'from':        request.GET.get('vs-glob-per',      ''),
        'employers':   request.GET.get('vs-glob-emp-id',   '')
    }

    if not search_query['year']:
        year = DT.datetime.now().year
    else:
        year = search_query['year']

    vacation = VacShedItems.objects.filter(bound_shed__year=year).order_by('bound_shed__dep__name', 'emp__fullname', 'dur_from')

    if int(search_query['department']) != 0:
        dep_id = search_query['department']
        department = TurvDepartments.objects.get(id=dep_id)

        if department.name == 'АУП':
            vacation = vacation.filter(emp__department_id=4) | vacation.filter(emp__department_id=31)
        else:
        
            if department.is_aup:
                vacation = vacation.filter(emp__aup_id = dep_id)
            else:
                vacation = vacation.filter(bound_shed__dep_id = dep_id)
    
    if search_query['position']:
        vacation = vacation.filter(emp__position__name__icontains=search_query['position'])

    if int(search_query['filial']) != 0:
        if int(search_query['filial']) == 1:
            vacation = vacation.filter(Q(bound_shed__dep__name__icontains='Центральный') | Q(bound_shed__dep__name__icontains='Быстринский'))

        if int(search_query['filial']) == 2:
            vacation = vacation.filter(bound_shed__dep__name__icontains='Быстринский')       
        
        if int(search_query['filial']) == 3:
            vacation = vacation.filter(bound_shed__dep__name__icontains='Центральный')
    
    if int(search_query['territory']) != 0:
        if int(search_query['territory']) == 1:
            vacation = vacation.filter(~Q(emp__aup__name__icontains='Елизово')) & vacation.filter(~Q(bound_shed__dep__name__icontains='Елизово')) & vacation.filter(~Q(emp__department__name__icontains='Елизово')) & vacation.filter(~Q(bound_shed__dep__name__icontains='Быстринский')) & vacation.filter(~Q(bound_shed__dep__name__icontains='Центральный'))
        if int(search_query['territory']) == 2:
            vacation = vacation.filter(emp__aup__name__icontains='Елизово') | vacation.filter(bound_shed__dep__name__icontains='Елизово') | vacation.filter(emp__department__name__icontains='Елизово')

    if int(search_query['from']) != 0:
       period = search_query['from']
       vacation = vacation.filter(dur_from__month=period).filter(move_from=None) | vacation.filter(move_from__month=period)
    #    vacation = vacation.filter(dur_from__month=period) | vacation.filter(move_from__month=period)

    if search_query['employers']:
        employers = str(search_query['employers']).split(',')
        employers.pop()
        vacation = VacShedItems.objects.filter(bound_shed__year=year).filter(emp_id__in=employers).order_by('bound_shed__dep__name', 'emp__fullname', 'dur_from')


    vacation = list(vacation.values('id', 'emp__department__name' , 'emp__aup__name' ,'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name', 'comm').order_by('emp__department__name', 'emp__aup__name', 'dur_from'))
    
    return JsonResponse(vacation, safe=False)