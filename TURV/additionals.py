from .models import TabelItem, Position, Employers

def search_tabel_item(search_query: dict):
    items = TabelItem.objects.filter(bound_tabel_id=search_query['tabel_id']).filter(
        employer__fullname__icontains=search_query['name']).filter(
        employer__position__name__icontains=search_query['position']).order_by(
        'employer__fullname')
    
    return items

def search_position(search_query: dict):
    items = Position.objects.filter(name__icontains=search_query['name']).order_by('name')

    return items

def search_employers(search_query: dict):
        if search_query['department_permission'] != 'all':
           items = Employers.objects.filter(department_id__in=search_query['department_permission'])
        else:
            items = Employers.objects.all()

        if search_query['name']:
            items = items.filter(fullname__icontains = search_query['name'])
        if search_query['department']:
            items = items.filter(department_id = search_query['department'])
        if search_query['shift']:
            if int(search_query['shift']) == 1:
                items = items.filter(shift_personnel=1)
            if int(search_query['shift']) == 2:
                items = items.filter(shift_personnel=0)
        if search_query['in_fired']:
            items = items.filter(fired=1)
        else:
            items = items.filter(fired=0)
        
        items.order_by('fullname')

        return items
    
