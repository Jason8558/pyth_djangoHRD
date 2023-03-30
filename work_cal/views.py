from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
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

# Create your views here.
