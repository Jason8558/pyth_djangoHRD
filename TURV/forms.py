from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT
from reg_jounals.models import logs, logs_event

class TabelItem_form(forms.ModelForm):
        class Meta:
            model = TabelItem
            fields = [
            'employer',
            'toxic_p',
            'auto',
            'type_time1',
            'type_time2',
            'type_time3',
            'type_time4',
            'type_time5',
            'type_time6',
            'type_time7',
            'type_time8',
            'type_time9',
            'type_time10',
            'type_time11',
            'type_time12',
            'type_time13',
            'type_time14',
            'type_time15',
            'type_time16',
            'type_time17',
            'type_time18',
            'type_time19',
            'type_time20',
            'type_time21',
            'type_time22',
            'type_time23',
            'type_time24',
            'type_time25',
            'type_time26',
            'type_time27',
            'type_time28',
            'type_time29',
            'type_time30',
            'type_time31',
            'hours1',
            'hours2',
            'hours3',
            'hours4',
            'hours5',
            'hours6',
            'hours7',
            'hours8',
            'hours9',
            'hours10',
            'hours11',
            'hours12',
            'hours13',
            'hours14',
            'hours15',
            'hours16',
            'hours17',
            'hours18',
            'hours19',
            'hours20',
            'hours21',
            'hours22',
            'hours23',
            'hours24',
            'hours25',
            'hours26',
            'hours27',
            'hours28',
            'hours29',
            'hours30',
            'hours31',
            'sHours1',
            'sHours2',
            'sHours3',
            'sHours4',
            'sHours5',
            'sHours6',
            'sHours7',
            'sHours8',
            'sHours9',
            'sHours10',
            'sHours11',
            'sHours12',
            'sHours13',
            'sHours14',
            'sHours15',
            'sHours16',
            'sHours17',
            'sHours18',
            'sHours19',
            'sHours20',
            'sHours21',
            'sHours22',
            'sHours23',
            'sHours24',
            'sHours25',
            'sHours26',
            'sHours27',
            'sHours28',
            'sHours29',
            'sHours30',
            'sHours31',
            'sHours32',
            'sHours33',
            'sHours34',
            'sHours35',
            'sHours37',
            'sHours38',
            'w_days',
            'w_hours',
            'v_days',
            'v_hours'
            ]

        auto = forms.ModelChoiceField(required=False, queryset=Automobile.objects.filter(used=1))


        type_time1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time6 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time7 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time8 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time9 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time10 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time11 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time12 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time13 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time14 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time15 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time16 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time17 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time18 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time19 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time20 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time21 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time22 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time23 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time24 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time25 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time26 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time27 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time28 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time29 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time30 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))
        type_time31 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'К', 'class': 'dig_code', 'type':'text'}))


        hours1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours6 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours7 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours8 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours9 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours10 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours11 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours12 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours13 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours14 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours15 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours16 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours17 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours18 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours19 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours20 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours21 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours22 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours23 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours24 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours25 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours26 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours27 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours28 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours29 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours30 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))
        hours31 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ч', 'class': 'dig_hours', 'type':'text'}))




        def saveFirst(self, bound_tabel):
            b_tabel = Tabel.objects.get(id=bound_tabel)
            emp = self.cleaned_data['employer']
            year_ = b_tabel.year
            month = b_tabel.month
            emp_name = emp.fullname
            emp_position = emp.position
            emp_level = emp.level
            emp_PoP = emp.positionOfPayment




            new_item = TabelItem.objects.create(

            bound_tabel_id = b_tabel.id,
            employer = emp,
            year = year_,
            month = month,
            type_time1 = self.cleaned_data['type_time1'],
            type_time2 = self.cleaned_data['type_time2'],
            type_time3 = self.cleaned_data['type_time3'],
            type_time4 = self.cleaned_data['type_time4'],
            type_time5 = self.cleaned_data['type_time5'],
            type_time6 = self.cleaned_data['type_time6'],
            type_time7 = self.cleaned_data['type_time7'],
            type_time8 = self.cleaned_data['type_time8'],
            type_time9 = self.cleaned_data['type_time9'],
            type_time10 = self.cleaned_data['type_time10'],
            type_time11 = self.cleaned_data['type_time11'],
            type_time12 = self.cleaned_data['type_time12'],
            type_time13 = self.cleaned_data['type_time13'],
            type_time14 = self.cleaned_data['type_time14'],
            type_time15 = self.cleaned_data['type_time15'],
            type_time16 = self.cleaned_data['type_time16'],
            type_time17 = self.cleaned_data['type_time17'],
            type_time18 = self.cleaned_data['type_time18'],
            type_time19 = self.cleaned_data['type_time19'],
            type_time20 = self.cleaned_data['type_time20'],
            type_time21 = self.cleaned_data['type_time21'],
            type_time22 = self.cleaned_data['type_time22'],
            type_time23 = self.cleaned_data['type_time23'],
            type_time24 = self.cleaned_data['type_time24'],
            type_time25 = self.cleaned_data['type_time25'],
            type_time26 = self.cleaned_data['type_time26'],
            type_time27 = self.cleaned_data['type_time27'],
            type_time28 = self.cleaned_data['type_time28'],
            type_time29 = self.cleaned_data['type_time29'],
            type_time30 = self.cleaned_data['type_time30'],
            type_time31 = self.cleaned_data['type_time31'],
            hours1 = self.cleaned_data['hours1'],
            hours2 = self.cleaned_data['hours2'],
            hours3 = self.cleaned_data['hours3'],
            hours4 = self.cleaned_data['hours4'],
            hours5 = self.cleaned_data['hours5'],
            hours6 = self.cleaned_data['hours6'],
            hours7 = self.cleaned_data['hours7'],
            hours8 = self.cleaned_data['hours8'],
            hours9 = self.cleaned_data['hours9'],
            hours10 = self.cleaned_data['hours10'],
            hours11 = self.cleaned_data['hours11'],
            hours12 = self.cleaned_data['hours12'],
            hours13 = self.cleaned_data['hours13'],
            hours14 = self.cleaned_data['hours14'],
            hours15 = self.cleaned_data['hours15'],
            hours16 = self.cleaned_data['hours16'],
            hours17 = self.cleaned_data['hours17'],
            hours18 = self.cleaned_data['hours18'],
            hours19 = self.cleaned_data['hours19'],
            hours20 = self.cleaned_data['hours20'],
            hours21 = self.cleaned_data['hours21'],
            hours22 = self.cleaned_data['hours22'],
            hours23 = self.cleaned_data['hours23'],
            hours24 = self.cleaned_data['hours24'],
            hours25 = self.cleaned_data['hours25'],
            hours26 = self.cleaned_data['hours26'],
            hours27 = self.cleaned_data['hours27'],
            hours28 = self.cleaned_data['hours28'],
            hours29 = self.cleaned_data['hours29'],
            hours30 = self.cleaned_data['hours30'],
            hours31 = self.cleaned_data['hours31'],
            sHours1 = self.cleaned_data['sHours1'],
            sHours2 = self.cleaned_data['sHours2'],
            sHours3 = self.cleaned_data['sHours3'],
            sHours4 = self.cleaned_data['sHours4'],
            sHours5 = self.cleaned_data['sHours5'],
            sHours6 = self.cleaned_data['sHours6'],
            sHours7 = self.cleaned_data['sHours7'],
            sHours8 = self.cleaned_data['sHours8'],
            sHours9 = self.cleaned_data['sHours9'],
            sHours10 = self.cleaned_data['sHours10'],
            sHours11 = self.cleaned_data['sHours11'],
            sHours12 = self.cleaned_data['sHours12'],
            sHours13 = self.cleaned_data['sHours13'],
            sHours14 = self.cleaned_data['sHours14'],
            sHours15 = self.cleaned_data['sHours15'],
            sHours16 = self.cleaned_data['sHours16'],
            sHours17 = self.cleaned_data['sHours17'],
            sHours18 = self.cleaned_data['sHours18'],
            sHours19 = self.cleaned_data['sHours19'],
            sHours20 = self.cleaned_data['sHours20'],
            sHours21 = self.cleaned_data['sHours21'],
            sHours22 = self.cleaned_data['sHours22'],
            sHours23 = self.cleaned_data['sHours23'],
            sHours24 = self.cleaned_data['sHours24'],
            sHours25 = self.cleaned_data['sHours25'],
            sHours26 = self.cleaned_data['sHours26'],
            sHours27 = self.cleaned_data['sHours27'],
            sHours28 = self.cleaned_data['sHours28'],
            sHours29 = self.cleaned_data['sHours29'],
            sHours30 = self.cleaned_data['sHours30'],
            sHours31 = self.cleaned_data['sHours31'],
            sHours32 = self.cleaned_data['sHours32'],
            sHours33 = self.cleaned_data['sHours33'],
            sHours34 = self.cleaned_data['sHours34'],
            sHours35 = self.cleaned_data['sHours35'],
            sHours38 = self.cleaned_data['sHours38'],
            w_days = self.cleaned_data['w_days'],
            w_hours = self.cleaned_data['w_hours'],
            v_days = self.cleaned_data['v_days'],
            v_hours = self.cleaned_data['v_hours'],
            toxic_p = self.cleaned_data['toxic_p'],
            auto = self.cleaned_data['auto']



            )

            return new_item

class Tabel_form(forms.ModelForm):
    class Meta:
        model = Tabel
        fields = ['year', 'month', 'department', 'del_check', 'sup_check', 'type']

    year = forms.CharField(label="Год (ТОЛЬКО 4 ЦИФРЫ!)", widget=forms.NumberInput(attrs={'maxlength':'4'}))
    def saveFirst(self, user_):

        next_id = int(Tabel.objects.latest('id').id) + 1
        logs.objects.create(
            date = DT.datetime.now(),
            event = logs_event.objects.get(id=3),
            doc_id = next_id,
            type = 'Табель',
            number = next_id,
            year = self.cleaned_data['year'],
            doc_date = DT.datetime.strptime(str(self.cleaned_data['year'] + '-' + self.cleaned_data['month'] + '-' + str(DT.datetime.now().day)), '%Y-%M-%d'),
            addData = 'Табель: '+ str(self.cleaned_data['department'].name) + ' за: ' + str(self.cleaned_data['month']) + ' ' + str(self.cleaned_data['year']) ,
            link = '/turv/create' + str(next_id),
            res_officer = user_)

        new_tabel = Tabel.objects.create(
            year = self.cleaned_data['year'],
            month = self.cleaned_data['month'],
            department = self.cleaned_data['department'],
            type = self.cleaned_data['type'],
            res_officer = user_)

        return new_tabel

class Employer_form(forms.ModelForm):
    class Meta:
        model = Employers
        fields = ['fullname', 'sex', 'position', 'department', 'level', 'positionOfPayment', 'shift_personnel', 'stand_worktime', 'fired']

    def saveFirst(self):
        if len(str(self.cleaned_data['fullname']).split(" ")) > 2:
            name = str(self.cleaned_data['fullname']).split(" ")
            lastname = str(name[0]) + ' '
            firstname = str(name[1][0]) + '.'
            middlename = str(name[2][0]) + '.'
            fullname = str(lastname) + str(firstname) + str(middlename)
        else:
            fullname = self.cleaned_data['fullname']
        new_employer = Employers.objects.create(
            fullname  = fullname,
            sex = self.cleaned_data['sex'],
            position = self.cleaned_data['position'],
            shift_personnel = self.cleaned_data['shift_personnel'],
            fired = self.cleaned_data['fired'],
            stand_worktime = self.cleaned_data['stand_worktime'],
            department = self.cleaned_data['department'],
            level = self.cleaned_data['level'],
            positionOfPayment = self.cleaned_data['positionOfPayment']

    )
        return new_employer

class Position_form(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']

    def saveFirst(self):
        new_position = Position.objects.create(
            name = self.cleaned_data['name']
        )
        return new_position

class Automobile_form(forms.ModelForm):
    class Meta:
        model = Automobile
        fields = ['number', 'model', 'unite_p', 'used']
    def saveFirst(self):
        new_automobile = Automobile.objects.create(
        number = self.cleaned_data['number'],
        model = self.cleaned_data['model'],
        unite_p = self.cleaned_data['unite_p'],
        used = self.cleaned_data['used']
        )
        return new_automobile
