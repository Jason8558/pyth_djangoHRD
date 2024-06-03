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

    vacation = VacShedItems.objects.filter(bound_shed__year=search_query['year']).order_by('bound_shed__dep__name', 'emp__fullname', 'dur_from')

    if search_query['department']:
        dep_id = search_query['department']
        
        if TurvDepartments.objects.get(id=dep_id).is_aup:
            vacation = vacation.filter(emp__aup_id = dep_id)
        else:
            vacation = vacation.filter(bound_shed__dep_id = dep_id)
    
    if search_query['position']:
        vacation = vacation.filter(emp__position__name__icontains=search_query['position'])

    if search_query['filial']:
        if int(search_query['filial']) == 1:
            vacation = vacation.filter(Q(bound_shed__dep__name__icontains='Мильково') | Q(bound_shed__dep__name__icontains='Эссо'))

        if int(search_query['filial']) == 2:
            vacation = vacation.filter(bound_shed__dep__name__icontains='Быстринский')       
        
        if int(search_query['filial']) == 3:
            vacation = vacation.filter(bound_shed__dep__name__icontains='Центральный')
    
    if search_query['territory']:
        if int(search_query['territory']) == 1:
            vacation = vacation.filter(~Q(emp__aup__name__icontains='Елизово'))
        if int(search_query['territory']) == 2:
            vacation = vacation.filter(emp__aup__name__icontains='Елизово')

    if search_query['from']:
       period = search_query['from']
       vacation = vacation.filter(dur_from__month=period) | vacation.filter(move_from__month=period)

    if search_query['employers']:
        employers = str(search_query['employers']).split(',')
        vacation = vacation.filter(emp_id__in=employers)


    vacation = list(vacation.values())
    
    return JsonResponse(vacation, safe=False)