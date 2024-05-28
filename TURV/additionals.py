from .models import TabelItem

def search_tabel_item(search_query: dict):
    items = TabelItem.objects.filter(bound_tabel_id=search_query['tabel_id']).filter(
        employer__fullname__icontains=search_query['name']).filter(
        employer__position__name__icontains=search_query['position']).order_by(
        'employer__fullname')
    
    return items
    
