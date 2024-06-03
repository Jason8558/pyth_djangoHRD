from .models import VacantionShedule as VacationShedules

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
        'year':        request.GET.get('vs-glob-year',     DT.datetime.now(year)),
        'department':  request.GET.get('vs-glob-dep',      ''),
        'position':    request.GET.get('vs-glob-pos',      ''),
        'filial':      request.GET.get('vs-glob-fil',      ''),
        'territory':   request.GET.get('vs-glob-terr',     ''),
        'from':        request.GET.get('vs-glob-per',      ''),
        'employers':   request.GET.get('vs-glob-emp-id',   '')
    }

    return ''