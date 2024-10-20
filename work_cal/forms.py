from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT

class work_cal_form(forms.Form):

    year = forms.CharField(max_length=4,  label='Год')

    jan = forms.CharField(max_length=100,  label='Январь', required=False)
    feb = forms.CharField(max_length=100,   label='Февраль', required=False)
    mar = forms.CharField(max_length=100,   label='Март', required=False)
    apr = forms.CharField(max_length=100,   label='Апрель', required=False)
    may = forms.CharField(max_length=100,   label='Май', required=False)
    jun = forms.CharField(max_length=100,   label='Июнь', required=False)
    jul = forms.CharField(max_length=100,   label='Июль', required=False)
    aug = forms.CharField(max_length=100,   label='Август', required=False)
    sep = forms.CharField(max_length=100,   label='Сентябрь', required=False)
    oct = forms.CharField(max_length=100,   label='Октябрь', required=False)
    nov = forms.CharField(max_length=100,   label='Ноябрь', required=False)
    dec = forms.CharField(max_length=100,   label='Декабрь', required=False)

    def save(self):
        months = {'1':'jan','2':"feb",'3':"mar",'4':"apr",'5':"may",'6':"jun",'7':"jul",'8':"aug",'9':"sep",'10':"oct",'11':"nov",'12':"dec"}
        for k,v in months.items():
            WorkCalendarRecord.objects.create(
               year = self.cleaned_data['year'],
               month = k,
               days = self.cleaned_data[v] 
            )
    
    def upd(self, year):
        year_for_update = year
        cal = WorkCalendarRecord.objects.filter(year=year)
        months = {'1':'jan','2':"feb",'3':"mar",'4':"apr",'5':"may",'6':"jun",'7':"jul",'8':"aug",'9':"sep",'10':"oct",'11':"nov",'12':"dec"}
        for i in range(1,13):
            obj = cal.filter(month=i)
            if obj:
                obj[0].days = self.cleaned_data[str(months[str(i)])]
                obj[0].save()




