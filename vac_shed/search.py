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