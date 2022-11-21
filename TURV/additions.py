from .models import *

def total_tabels(deps, month, year):
    table = list()
    for dep in deps:
        tabeltypes = dep.conftype.all()
        tabels = list()
        for type in tabeltypes:
            tabel = Tabel.objects.filter(department_id=dep.id).filter(type_id=type.id).filter(month=month).filter(year=year).filter(iscorr=0).filter(del_check=0)
            print(len(tabel))
            if len(tabel) == 0:
                tabels.append({
                type.id:'',
                'sup_check':'',
                'paper_check':''
                })
            else:
                tabels.append({
                type.id:tabel.latest('id').id,
                'sup_check':tabel.latest('id').sup_check,
                'paper_check':tabel.latest('id').paper_check
                })




        table.append({
        'depid':dep.id,
        'dep':dep.name,
        'tabels':tabels
        })

    return table
