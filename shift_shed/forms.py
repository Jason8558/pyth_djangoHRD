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
    # emps = forms.ModelChoiceField(required=True, queryset=Employers.objects.none(),widget=forms.Select(
    #     attrs={'class': 'chosen-select'}))
    dep = forms.ModelChoiceField(required=True, label="Подразделение: ", queryset=Department.objects.none(), widget=forms.Select(
        attrs={'onclick': 'getemps()'}))
    # emps_list = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'hidden_field'}))

    def save(self, commit: bool = ...) -> any:
        return super().save(commit)


    # def saveAll(self):
    #     months = [1,2,3,4,5,6,7,8,9,10,11,12]
    #     new_shed = ShiftShedModel.objects.create(
    #     year = self.cleaned_data['year'],
    #     dep = self.cleaned_data['dep']
    #     )
    #     emps = self.cleaned_data['emps_list'].split(',')
    #     shedule = addition_sheditem(emps, self.cleaned_data['year'])
    #     shed = ShiftShedModel.objects.latest('id')
    #     for m in months:
    #         for s in shedule:

    #             if m == s['month']:
    #                 ShiftShedItem.objects.create(
    #                 employer = s['emp'],
    #                 bound_shed = shed,
    #                 month = s['month']
    #                 )
    #                 ss_item = ShiftShedItem.objects.latest('id')
    #                 for day in s['days']:
    #                      setattr(ss_item, 'day_'+str(day), 'ОТ')
    #                 ss_item.save()


        

        # return new_shed


class SS_AddItem_form(forms.ModelForm):
    class Meta:
        model = ShiftShedItem
        fields = ['bound_shed',
            'employer',
    'month',
    'day_1',
    'day_2',
    'day_3',
    'day_4',
    'day_5',
    'day_6',
    'day_7',
    'day_8',
    'day_9',
    'day_10',
    'day_11',
    'day_12',
    'day_13',
    'day_14',
    'day_15',
    'day_16',
    'day_17',
    'day_18',
    'day_19',
    'day_20',
    'day_21',
    'day_22',
    'day_23',
    'day_24',
    'day_25',
    'day_26',
    'day_27',
    'day_28',
    'day_29',
    'day_30',
    'day_31',
    'fact',
    'celeb',
    'deviation',
    'norma']
    
    day_1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_6 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_7 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_8 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_9 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_10 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_11 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_12 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_13 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_14 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_15 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_16 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_17 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_18 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_19 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_20 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_21 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_22 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_23 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_24 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_25 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_26 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_27 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_28 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_29 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_30 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))
    day_31 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ОТ\Ч', 'class': 'dig_code', 'type':'text'}))

    def saveFirst(self,shed, month):
       
       if self.cleaned_data['deviation'] == '':
           dev = 0
       else:
           dev = self.cleaned_data['deviation']

       new_item = ShiftShedItem.objects.create (
            bound_shed_id = shed,
            month = month,
            employer = self.cleaned_data['employer'],
            day_1 = self.cleaned_data['day_1'],
            day_2 = self.cleaned_data['day_2'],
            day_3 = self.cleaned_data['day_3'],
            day_4 = self.cleaned_data['day_4'],
            day_5 = self.cleaned_data['day_5'],
            day_6 = self.cleaned_data['day_6'],
            day_7 = self.cleaned_data['day_7'],
            day_8 = self.cleaned_data['day_8'],
            day_9 = self.cleaned_data['day_9'],
            day_10 = self.cleaned_data['day_10'],
            day_11 = self.cleaned_data['day_11'],
            day_12 = self.cleaned_data['day_12'],
            day_13 = self.cleaned_data['day_13'],
            day_14 = self.cleaned_data['day_14'],
            day_15 = self.cleaned_data['day_15'],
            day_16 = self.cleaned_data['day_16'],
            day_17 = self.cleaned_data['day_17'],
            day_18 = self.cleaned_data['day_18'],
            day_19 = self.cleaned_data['day_19'],
            day_20 = self.cleaned_data['day_20'],
            day_21 = self.cleaned_data['day_21'],
            day_22 = self.cleaned_data['day_22'],
            day_23 = self.cleaned_data['day_23'],
            day_24 = self.cleaned_data['day_24'],
            day_25 = self.cleaned_data['day_25'],
            day_26 = self.cleaned_data['day_26'],
            day_27 = self.cleaned_data['day_27'],
            day_28 = self.cleaned_data['day_28'],
            day_29 = self.cleaned_data['day_29'],
            day_30 = self.cleaned_data['day_30'],
            day_31 = self.cleaned_data['day_31'],
            fact = self.cleaned_data['fact'],
            celeb = self.cleaned_data['celeb'],

            deviation = dev,
            norma = self.cleaned_data['norma']

        )
    