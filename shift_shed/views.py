from django.shortcuts import render
from .models import *
from .forms import *
from TURV.models import TabelItem
from TURV.models import Department
from django.http import HttpResponse, JsonResponse

def ss_main(request):
    if request.user.is_authenticated:
        ss = ShiftShedModel.objects.all()
        return render(request, 'shift_shed/ss-main.html', context={'ss':ss})

def ss_create(request):
    if request.user.is_authenticated:
        form = ShiftShed_form(request.GET)
        form.fields['dep'].queryset = Department.objects.filter(user=request.user)
        return render(request, 'shift_shed/create.html', context={'form':form})

def ss_get_employers(request, dep):
    if request.user.is_authenticated:
        emps = Employers.objects.values('id','fullname','position__name').filter(mainworkplace=1).filter(fired=0).filter(department=dep)
        emps = list(emps)
        return JsonResponse(emps, safe=False)
