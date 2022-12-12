from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import *
from .additionals import *
from TURV.models import Department
from TURV.models import Employers
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT


class ShiftShed_form(forms.ModelForm):
    class Meta:
        model = ShiftShedModel
        fields = ['dep', 'year']
    emps = forms.ModelChoiceField(required=True, queryset=Employers.objects.none(),widget=forms.Select(
        attrs={'class': 'chosen-select'}))
    dep = forms.ModelChoiceField(required=True, queryset=Department.objects.none(), widget=forms.Select(
        attrs={'onclick': 'getemps()'}))
    emps_list = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'hidden_field'}))

    def saveAll(self):
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        new_shed = ShiftShedModel.objects.create(
        year = self.cleaned_data['year'],
        dep = self.cleaned_data['dep']
        )
        emps = self.cleaned_data['emps_list'].split(',')
        shedule = addition_sheditem(emps, self.cleaned_data['year'])
        shed = ShiftShedModel.objects.latest('id')
        for m in months:
            for s in shedule:
                print(s)
                if m == s['month']:
                    ShiftShedItem.objects.create(
                    employer = s['emp'],
                    bound_shed = shed,
                    month = s['month']
                    )

                    ss_item = ShiftShedItem.objects.latest('id')
                    for day in s['days']:
                         setattr(ss_item, 'day_'+str(day), 'ОТ')

                    ss_item.save()
        return new_shed




# class ShiftShedItem_form(forms.ModelForm):
#     class Meta:
#         model = ShiftShedModel
#         fields = ['employer',
#     'month',
#     'day_1',
#     'day_2',
#     'day_3',
#     'day_4',
#     'day_5',
#     'day_6',
#     'day_7',
#     'day_8',
#     'day_9',
#     'day_10',
#     'day_11',
#     'day_12',
#     'day_13',
#     'day_14',
#     'day_15',
#     'day_16',
#     'day_17',
#     'day_18',
#     'day_19',
#     'day_20',
#     'day_21',
#     'day_22',
#     'day_23',
#     'day_24',
#     'day_25',
#     'day_26',
#     'day_27',
#     'day_28',
#     'day_29',
#     'day_30',
#     'day_31']
