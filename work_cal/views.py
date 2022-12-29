from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

def get_cal(request, year):
    if request.user.is_authenticated:
        calendar = WorkCalendarRecord.objects.filter(year=year).values('year','month','days')
        calendar = list(calendar)

        return JsonResponse(calendar, safe=False)

# Create your views here.
