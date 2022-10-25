from vac_shed.models import VacantionShedule, VacantionSheduleItem

vseds = VacantionShedule.objects.filter(year=2023)

for v in vseds:
    items = VacantionSheduleItem.objects.filter(bound_shed_id=v.id)
    if len(items) < 2:
        print(v.dep.name)
