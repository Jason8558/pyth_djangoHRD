from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def get_cal(request, year):
    if request.user.is_authenticated:
        calendar = WorkCalendarRecord.objects.filter(year=year).values('year','month','days')
        calendar = list(calendar)

        return JsonResponse(calendar, safe=False)


@login_required
def get_month(request, year, month):
    month = WorkCalendarRecord.objects.filter(year=year).filter(month=month).values('days')
    days = list()
    for day in month:
        days.append(day)
    return JsonResponse(days, safe=False)

@login_required
def new_record(request):
    if request.method == 'GET':
        form = work_cal_form(request.GET)
        return render(request, 'work_cal\record.html', context={'form':form})
    else:
        form = work_cal_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/turv')

@login_required
def upd_record(request, year):
    init = dict()
    months = {'1':'jan','2':"feb",'3':"mar",'4':"apr",'5':"may",'6':"jun",'7':"jul",'8':"aug",'9':"sep",'10':"oct",'11':"nov",'12':"dec"}

    cal = WorkCalendarRecord.objects.filter(year=year)

    if request.method == 'GET':
        for i in range(1,13):
            rec = cal.filter(month=i)
            if rec:
                init[months[str(i)]] = rec[0].days
        init['year'] = year

        form = work_cal_form(initial=init)
        return render(request, 'work_cal/record.html', context={'form':form})
    else:
        form = work_cal_form(request.POST)
        if form.is_valid():
            form.upd(year)
            return redirect('.')
        else:
            errs = form.errors.as_ul()
            return render(request, 'work_cal/record.html', context={'form':form, 'errs':errs})
        

        

    


@login_required
def calendar_list(request):
    cal = WorkCalendarRecord.objects.values('year').distinct()
    return render(request, 'work_cal/list.html', context={'cal':cal})

@login_required
def clear(request, year):
    cal = WorkCalendarRecord.objects.filter(year=year).delete()
    return redirect('/work_cal')

@login_required
def get_cal_html(request, year):
    calendar_data = WorkCalendarRecord.objects.filter(year=year).order_by('month')
    calendar = list()
    months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
    for cd in calendar_data:
        calendar.append({
            'month_text':months[str(cd.month)],
            'month':cd.month,
            'days': cd.days
            })
    return render(request, 'work_cal/getcal.html', context={'cal':calendar, 'year':year})

# class WorkCalAPI(APIView):
#     def get(self, request):
#         queryset = WorkCalendarRecord.objects.all().values()
#         return Response({'cal':list(queryset)})
    
#     def post(self, request):
#         return Response({'i can by myself flowers':'write my name in a sand'})

       
        
