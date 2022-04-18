from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

def ugroup(request):
        # Проверка на права пользователя
        user_ = request.user
        u_group = user_.groups.all()

        granted = False
        for group in u_group:
            if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
                granted = True

        if request.user.is_superuser:
            granted = True
        return granted


def vacsheds(request):
    if request.user.is_authenticated:
        if ugroup(request) == True:
            vacsheds = VacantionShedule.objects.all()
        return render(request, 'VacShed/index.html', context={'vacsheds':vacsheds})
    else:
        return redirect('/accounts/login/')

def vacshed_create(request,vs):
    if request.user.is_authenticated:
        vacshed = VacantionShedule.objects.get(id=vs)

        return render(request, 'VacShed/vs-create.html', context={'vacshed':vacshed})

def getvacshed_json(request, vs):
    if request.user.is_authenticated:
        items = VacantionSheduleItem.objects.filter(bound_shed=vs).values('id', 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count').order_by('emp', 'dur_from')
        items = list(items)
        return JsonResponse(items, safe=False)
